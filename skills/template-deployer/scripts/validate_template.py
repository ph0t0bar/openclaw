#!/usr/bin/env python3
"""
Template Validator - Validate email templates for deployment
Part of template-deployer skill
"""

import argparse
import re
import sys
from pathlib import Path

WORKSPACE_ROOT = Path("/root/.openclaw/workspace")
TEMPLATES_DIR = WORKSPACE_ROOT / "templates"

def validate_html_structure(content):
    """Validate basic HTML structure"""
    issues = []
    
    # Check DOCTYPE
    if not content.strip().startswith('<!DOCTYPE html>'):
        issues.append("Missing or incorrect DOCTYPE declaration")
    
    # Check required HTML elements
    required = {
        '<html': 'Missing <html> tag',
        '<head': 'Missing <head> section', 
        '<body': 'Missing <body> section',
        '<title': 'Missing <title> tag'
    }
    
    for tag, message in required.items():
        if tag.lower() not in content.lower():
            issues.append(message)
    
    return issues

def validate_email_compatibility(content):
    """Check email client compatibility"""
    issues = []
    
    # Check for problematic elements
    problematic = [
        ('<script', 'JavaScript not supported in most email clients'),
        ('<iframe', 'iFrames not supported in email'),
        ('<embed', 'Embed tags not supported in email'),
        ('<object', 'Object tags not supported in email'),
        ('position: fixed', 'Fixed positioning not supported in email'),
        ('position: absolute', 'Absolute positioning limited in email'),
        ('background-attachment', 'Background attachment not widely supported')
    ]
    
    for element, message in problematic:
        if element.lower() in content.lower():
            issues.append(message)
    
    # Check for inline CSS preference
    style_tags = len(re.findall(r'<style[^>]*>', content, re.IGNORECASE))
    style_attributes = len(re.findall(r'style\s*=', content, re.IGNORECASE))
    
    if style_tags > 0 and style_attributes == 0:
        issues.append("Consider using inline CSS for better email client support")
    
    return issues

def validate_brooke_theme(content):
    """Check Brooke theme compliance"""
    issues = []
    
    # Brooke theme colors
    brooke_colors = {
        '#f9f7f4': 'cream background',
        '#8d9f87': 'sage green',
        '#d4854c': 'copper accent',
        '#2d3748': 'dark text',
        '#4a5568': 'medium text'
    }
    
    # Check for theme colors
    found_colors = []
    for color, description in brooke_colors.items():
        if color.lower() in content.lower():
            found_colors.append(description)
    
    # Also check for color names
    color_names = ['cream', 'sage', 'copper']
    for color in color_names:
        if color in content.lower():
            found_colors.append(color)
    
    if not found_colors:
        issues.append("No Brooke theme colors detected. Expected: cream/sage/copper palette")
    else:
        print(f"✅ Brooke theme colors found: {', '.join(found_colors)}")
    
    # Check for Newsreader font (Brooke theme standard)
    if 'newsreader' not in content.lower():
        issues.append("Consider using Newsreader font for Brooke theme compliance")
    
    return issues

def validate_responsive_design(content):
    """Check responsive design elements"""
    issues = []
    
    # Check for viewport meta tag
    if 'viewport' not in content.lower():
        issues.append("Missing viewport meta tag for mobile responsiveness")
    
    # Check for media queries
    if '@media' not in content.lower():
        issues.append("No media queries found. Consider adding responsive styles.")
    
    # Check for table-based layout (common for email)
    if '<table' not in content.lower():
        issues.append("Consider using table-based layout for email compatibility")
    
    return issues

def validate_required_sections(content):
    """Check for required email sections"""
    issues = []
    
    # Common email sections
    sections = {
        'header': ['header', 'logo', 'masthead'],
        'footer': ['footer', 'unsubscribe', 'contact'],
        'content': ['main', 'content', 'body']
    }
    
    for section, keywords in sections.items():
        found = any(keyword in content.lower() for keyword in keywords)
        if not found:
            issues.append(f"Missing {section} section (looked for: {', '.join(keywords)})")
    
    return issues

def check_file_size(content):
    """Check template file size"""
    issues = []
    
    size_bytes = len(content.encode('utf-8'))
    size_kb = size_bytes / 1024
    
    # Gmail clips emails over 102KB
    if size_bytes > 102 * 1024:
        issues.append(f"Template is {size_kb:.1f}KB. Gmail clips emails over 102KB.")
    elif size_bytes > 50 * 1024:
        issues.append(f"Template is {size_kb:.1f}KB. Consider optimization for faster loading.")
    
    print(f"📊 Template size: {size_kb:.1f}KB ({size_bytes:,} bytes)")
    
    return issues

def main():
    parser = argparse.ArgumentParser(description="Validate email template")
    parser.add_argument('--template', type=str, required=True, help="Template filename")
    parser.add_argument('--strict', action='store_true', help="Strict validation (warnings become errors)")
    
    args = parser.parse_args()
    
    template_path = TEMPLATES_DIR / args.template
    
    if not template_path.exists():
        print(f"❌ Template not found: {template_path}")
        return 1
    
    print(f"🔍 Validating template: {template_path}")
    
    # Read template content
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        print("❌ Template contains non-UTF-8 characters")
        return 1
    
    # Run all validations
    all_issues = []
    
    print("\n📋 Running validation checks...")
    
    # HTML Structure
    issues = validate_html_structure(content)
    if issues:
        print("⚠️  HTML Structure issues:")
        for issue in issues:
            print(f"   - {issue}")
        all_issues.extend(issues)
    else:
        print("✅ HTML structure valid")
    
    # Email Compatibility  
    issues = validate_email_compatibility(content)
    if issues:
        print("⚠️  Email compatibility issues:")
        for issue in issues:
            print(f"   - {issue}")
        all_issues.extend(issues)
    else:
        print("✅ Email compatibility good")
    
    # Brooke Theme
    issues = validate_brooke_theme(content)
    if issues:
        print("⚠️  Brooke theme issues:")
        for issue in issues:
            print(f"   - {issue}")
        all_issues.extend(issues)
    else:
        print("✅ Brooke theme compliant")
    
    # Responsive Design
    issues = validate_responsive_design(content)
    if issues:
        print("⚠️  Responsive design issues:")
        for issue in issues:
            print(f"   - {issue}")
        all_issues.extend(issues)
    else:
        print("✅ Responsive design elements found")
    
    # Required Sections
    issues = validate_required_sections(content)
    if issues:
        print("⚠️  Section issues:")
        for issue in issues:
            print(f"   - {issue}")
        all_issues.extend(issues)
    else:
        print("✅ Required sections present")
    
    # File Size
    issues = check_file_size(content)
    if issues:
        print("⚠️  File size issues:")
        for issue in issues:
            print(f"   - {issue}")
        all_issues.extend(issues)
    
    # Summary
    print(f"\n📊 Validation complete:")
    print(f"   Template: {args.template}")
    print(f"   Size: {len(content):,} characters")
    print(f"   Issues: {len(all_issues)}")
    
    if all_issues:
        if args.strict:
            print("\n❌ Validation failed (strict mode)")
            return 1
        else:
            print(f"\n⚠️  {len(all_issues)} issues found (warnings)")
            return 0
    else:
        print("\n✅ Template validation passed!")
        return 0

if __name__ == "__main__":
    sys.exit(main())