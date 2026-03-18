#!/usr/bin/env python3
"""
Template Validator - Validates email template structure and requirements
Prevents deployment of broken templates that cause agent crisis loops
"""

import os
import sys
import json
import re
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse

class TemplateValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.errors = []
        self.warnings = []
        self.required_sections = set()
        self.found_sections = set()
        self.links = []
        self.images = []
        self.current_tag = None
        
    def handle_starttag(self, tag, attrs):
        self.current_tag = tag
        attrs_dict = dict(attrs)
        
        # Check for required sections
        if tag == 'div' and 'class' in attrs_dict:
            classes = attrs_dict['class'].split()
            for cls in classes:
                if cls in ['header', 'content', 'footer', 'digest-item', 'title-section']:
                    self.found_sections.add(cls)
                    
        # Collect links and images for validation
        if tag == 'a' and 'href' in attrs_dict:
            self.links.append(attrs_dict['href'])
        elif tag == 'img' and 'src' in attrs_dict:
            self.images.append(attrs_dict['src'])
            
        # Check for inline styles (should be minimal)
        if 'style' in attrs_dict and len(attrs_dict['style']) > 100:
            self.warnings.append(f"Large inline style on {tag} - consider CSS classes")
            
    def validate_structure(self):
        """Validate basic HTML structure"""
        # Define required sections for email templates
        self.required_sections = {'header', 'content', 'footer'}
        
        missing_sections = self.required_sections - self.found_sections
        if missing_sections:
            self.errors.append(f"Missing required sections: {', '.join(missing_sections)}")
            
    def validate_links(self):
        """Validate all links are properly formatted"""
        for link in self.links:
            if not link.startswith(('http://', 'https://', 'mailto:', '#')):
                self.warnings.append(f"Suspicious link format: {link}")
                
    def validate_images(self):
        """Validate image sources"""
        for img_src in self.images:
            if not img_src.startswith(('http://', 'https://', 'data:')):
                self.warnings.append(f"Local image path may not work in email: {img_src}")

def validate_template_file(template_path):
    """Main validation function"""
    if not os.path.exists(template_path):
        return {
            'valid': False,
            'errors': [f"Template file not found: {template_path}"],
            'warnings': []
        }
        
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return {
            'valid': False,
            'errors': [f"Could not read template file: {str(e)}"],
            'warnings': []
        }
        
    # Basic size check
    size_kb = len(content) / 1024
    warnings = []
    if size_kb > 200:
        warnings.append(f"Template size is {size_kb:.1f}KB - may be too large for email")
        
    # HTML validation
    validator = TemplateValidator()
    try:
        validator.feed(content)
        validator.validate_structure()
        validator.validate_links()
        validator.validate_images()
    except Exception as e:
        return {
            'valid': False,
            'errors': [f"HTML parsing error: {str(e)}"],
            'warnings': warnings
        }
        
    # Check for common email template requirements
    errors = validator.errors
    
    # Must have DOCTYPE
    if not content.strip().startswith('<!DOCTYPE'):
        errors.append("Missing DOCTYPE declaration")
        
    # Should have viewport meta tag for mobile
    if 'viewport' not in content.lower():
        warnings.append("Missing viewport meta tag for mobile compatibility")
        
    # Check for table-based layout (recommended for email)
    if '<table' not in content.lower():
        warnings.append("No table layout detected - may not render well in all email clients")
        
    all_warnings = warnings + validator.warnings
    
    return {
        'valid': len(errors) == 0,
        'errors': errors,
        'warnings': all_warnings,
        'size_kb': round(size_kb, 1),
        'sections_found': list(validator.found_sections),
        'links_count': len(validator.links),
        'images_count': len(validator.images)
    }

def main():
    if len(sys.argv) < 2:
        print("Usage: python validate_template.py <template_path>")
        sys.exit(1)
        
    template_path = sys.argv[1]
    result = validate_template_file(template_path)
    
    # Always output JSON for script integration when requested
    if '--json' in sys.argv:
        print(json.dumps(result, indent=2))
        sys.exit(0 if result['valid'] else 1)
    
    print(f"Validating: {template_path}")
    print(f"Size: {result['size_kb']}KB")
    
    if result['valid']:
        print("✅ Template validation PASSED")
        print(f"Sections found: {', '.join(result['sections_found'])}")
        print(f"Links: {result['links_count']}, Images: {result['images_count']}")
    else:
        print("❌ Template validation FAILED")
        for error in result['errors']:
            print(f"  ERROR: {error}")
            
    if result['warnings']:
        print("\nWarnings:")
        for warning in result['warnings']:
            print(f"  WARNING: {warning}")
        
    sys.exit(0 if result['valid'] else 1)

if __name__ == '__main__':
    main()