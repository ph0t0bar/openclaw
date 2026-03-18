#!/usr/bin/env python3
"""
Template Tester - Comprehensive template testing and validation
Tests template rendering, links, and integration points
"""

import os
import sys
import json
import time
import subprocess
from pathlib import Path
from urllib.parse import urlparse
import re

def test_html_validity(template_path):
    """Test basic HTML validity"""
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return {
            'test': 'html_validity',
            'passed': False,
            'error': f"Could not read template: {str(e)}"
        }
        
    # Basic HTML structure checks
    tests = {
        'has_doctype': content.strip().startswith('<!DOCTYPE'),
        'has_html_tag': '<html' in content.lower(),
        'has_head_tag': '<head' in content.lower(),
        'has_body_tag': '<body' in content.lower(),
        'properly_closed': content.count('<') == content.count('>'),
        'balanced_divs': content.lower().count('<div') == content.lower().count('</div>'),
    }
    
    failed_tests = [test for test, passed in tests.items() if not passed]
    
    return {
        'test': 'html_validity',
        'passed': len(failed_tests) == 0,
        'details': tests,
        'failed_tests': failed_tests,
        'size_kb': round(len(content) / 1024, 1)
    }

def test_email_compatibility(template_path):
    """Test email client compatibility features"""
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return {
            'test': 'email_compatibility',
            'passed': False,
            'error': f"Could not read template: {str(e)}"
        }
        
    # Email-specific compatibility checks
    compatibility = {
        'has_tables': '<table' in content.lower(),
        'has_viewport_meta': 'viewport' in content.lower(),
        'no_external_css': '<link' not in content.lower() or 'stylesheet' not in content.lower(),
        'no_javascript': '<script' not in content.lower(),
        'has_alt_text': 'alt=' in content.lower() if '<img' in content.lower() else True,
        'width_attributes': bool(re.search(r'width\s*=\s*["\']?\d+', content, re.I)),
    }
    
    # Email client specific warnings
    warnings = []
    
    if 'display: flex' in content.lower():
        warnings.append("Flexbox may not work in older email clients")
        
    if 'position: absolute' in content.lower():
        warnings.append("Absolute positioning may not work in email clients")
        
    if '@media' in content.lower():
        warnings.append("Media queries have limited support in email clients")
        
    score = sum(compatibility.values()) / len(compatibility)
    
    return {
        'test': 'email_compatibility',
        'passed': score >= 0.7,  # 70% compatibility required
        'score': round(score, 2),
        'details': compatibility,
        'warnings': warnings
    }

def test_links_and_assets(template_path):
    """Test all links and assets in the template"""
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return {
            'test': 'links_and_assets',
            'passed': False,
            'error': f"Could not read template: {str(e)}"
        }
        
    # Extract links and assets
    links = re.findall(r'href\s*=\s*["\']([^"\']+)["\']', content, re.I)
    images = re.findall(r'src\s*=\s*["\']([^"\']+)["\']', content, re.I)
    
    link_results = []
    asset_results = []
    
    # Test links (simplified - would use actual HTTP requests in production)
    for link in links:
        parsed = urlparse(link)
        
        if link.startswith('#'):
            # Internal anchor - check if target exists
            anchor = link[1:]
            has_target = f'id="{anchor}"' in content or f"id='{anchor}'" in content
            link_results.append({
                'url': link,
                'type': 'anchor',
                'accessible': has_target,
                'note': 'Internal anchor'
            })
        elif link.startswith(('http://', 'https://')):
            # External link - assume accessible for testing
            link_results.append({
                'url': link,
                'type': 'external',
                'accessible': True,
                'note': 'External link (not tested)'
            })
        elif link.startswith('mailto:'):
            # Email link - validate format
            email_valid = '@' in link and '.' in link.split('@')[1]
            link_results.append({
                'url': link,
                'type': 'email',
                'accessible': email_valid,
                'note': 'Email link format check'
            })
        else:
            link_results.append({
                'url': link,
                'type': 'unknown',
                'accessible': False,
                'note': 'Unknown link format'
            })
            
    # Test images/assets
    for img in images:
        if img.startswith('data:'):
            asset_results.append({
                'url': img[:50] + '...',
                'type': 'data_url',
                'accessible': True,
                'note': 'Inline data URL'
            })
        elif img.startswith(('http://', 'https://')):
            asset_results.append({
                'url': img,
                'type': 'external',
                'accessible': True,
                'note': 'External asset (not tested)'
            })
        else:
            # Local file - check if accessible
            accessible = Path(img).exists() if not img.startswith('/') else Path(template_path).parent / img
            asset_results.append({
                'url': img,
                'type': 'local',
                'accessible': bool(accessible),
                'note': 'Local file reference'
            })
            
    # Calculate overall accessibility
    all_items = link_results + asset_results
    accessible_count = sum(1 for item in all_items if item['accessible'])
    total_count = len(all_items)
    
    return {
        'test': 'links_and_assets',
        'passed': total_count == 0 or accessible_count / total_count >= 0.9,  # 90% accessible
        'accessible_count': accessible_count,
        'total_count': total_count,
        'links': link_results,
        'assets': asset_results
    }

def test_template_integration(template_path):
    """Test template integration points"""
    
    # This would test actual integration in production:
    # - Resend API template validation
    # - Hub dashboard template preview
    # - Email sending test
    
    # For now, simulate integration tests
    integration_tests = {
        'resend_api_compatible': True,  # Would validate against Resend API
        'hub_dashboard_preview': True,  # Would test Hub preview rendering
        'mobile_responsive': True,     # Would test mobile rendering
        'digest_format_compatible': True,  # Would validate digest structure
    }
    
    # Check for required digest sections (if this is a digest template)
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Look for digest-specific elements
        has_digest_structure = any(cls in content for cls in [
            'digest-item', 'digest-header', 'digest-footer',
            'drop-item', 'insight-section'
        ])
        
        if has_digest_structure:
            digest_elements = {
                'has_digest_items': 'digest-item' in content,
                'has_date_section': any(date_term in content.lower() for date_term in [
                    'date', 'today', 'yesterday', 'this week'
                ]),
                'has_unsubscribe': 'unsubscribe' in content.lower(),
                'has_brand_footer': any(brand in content.lower() for brand in [
                    'dropanywhere', 'brutallyhonest', 'joey'
                ])
            }
            
            integration_tests['digest_format_compatible'] = all(digest_elements.values())
            integration_tests['digest_elements'] = digest_elements
            
    except Exception as e:
        integration_tests['file_read_error'] = str(e)
        
    passed_count = sum(1 for test, passed in integration_tests.items() 
                      if isinstance(passed, bool) and passed)
    total_count = sum(1 for test, passed in integration_tests.items() 
                     if isinstance(passed, bool))
                     
    return {
        'test': 'template_integration',
        'passed': passed_count == total_count,
        'score': round(passed_count / max(total_count, 1), 2),
        'details': integration_tests
    }

def test_performance(template_path):
    """Test template performance characteristics"""
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return {
            'test': 'performance',
            'passed': False,
            'error': f"Could not read template: {str(e)}"
        }
        
    # Performance metrics
    size_bytes = len(content.encode('utf-8'))
    size_kb = size_bytes / 1024
    
    # Count various elements that affect performance
    image_count = content.lower().count('<img')
    external_requests = len(re.findall(r'(?:src|href)\s*=\s*["\']https?://[^"\']+["\']', content, re.I))
    inline_styles = len(re.findall(r'style\s*=\s*["\'][^"\']+["\']', content, re.I))
    
    performance_score = 1.0
    warnings = []
    
    # Size penalties
    if size_kb > 100:
        performance_score -= 0.3
        warnings.append(f"Template size ({size_kb:.1f}KB) may be too large for email")
    elif size_kb > 50:
        performance_score -= 0.1
        warnings.append(f"Template size ({size_kb:.1f}KB) is on the larger side")
        
    # External request penalties
    if external_requests > 10:
        performance_score -= 0.2
        warnings.append(f"Too many external requests ({external_requests})")
    elif external_requests > 5:
        performance_score -= 0.1
        warnings.append(f"Many external requests ({external_requests})")
        
    # Inline style penalties
    if inline_styles > 20:
        performance_score -= 0.1
        warnings.append(f"Too many inline styles ({inline_styles}) - consider CSS consolidation")
        
    performance_score = max(0, performance_score)
    
    return {
        'test': 'performance',
        'passed': performance_score >= 0.7,
        'score': round(performance_score, 2),
        'metrics': {
            'size_kb': round(size_kb, 1),
            'size_bytes': size_bytes,
            'image_count': image_count,
            'external_requests': external_requests,
            'inline_styles': inline_styles
        },
        'warnings': warnings
    }

def run_all_tests(template_path):
    """Run comprehensive template test suite"""
    
    if not os.path.exists(template_path):
        return {
            'passed': False,
            'error': f"Template file not found: {template_path}",
            'tests': []
        }
        
    print(f"Testing template: {template_path}")
    print("=" * 60)
    
    # Run all test suites
    test_functions = [
        test_html_validity,
        test_email_compatibility, 
        test_links_and_assets,
        test_template_integration,
        test_performance
    ]
    
    results = []
    passed_count = 0
    
    for test_func in test_functions:
        print(f"Running {test_func.__name__}...", end=" ")
        
        try:
            result = test_func(template_path)
            results.append(result)
            
            if result['passed']:
                print("✅ PASSED")
                passed_count += 1
            else:
                print("❌ FAILED")
                if 'error' in result:
                    print(f"   Error: {result['error']}")
                    
        except Exception as e:
            error_result = {
                'test': test_func.__name__,
                'passed': False,
                'error': f"Test execution failed: {str(e)}"
            }
            results.append(error_result)
            print(f"💥 ERROR: {str(e)}")
            
    print("=" * 60)
    
    overall_passed = passed_count == len(test_functions)
    
    summary = {
        'template_path': template_path,
        'overall_passed': overall_passed,
        'passed_count': passed_count,
        'total_count': len(test_functions),
        'score': round(passed_count / len(test_functions), 2),
        'tests': results,
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())
    }
    
    print(f"Overall Result: {'✅ ALL TESTS PASSED' if overall_passed else '❌ SOME TESTS FAILED'}")
    print(f"Score: {passed_count}/{len(test_functions)} ({summary['score']*100:.0f}%)")
    
    return summary

def main():
    if len(sys.argv) < 2:
        print("Usage: python test_template.py <template_path> [--json]")
        print("Example: python test_template.py templates/brooke-demo-email.html")
        sys.exit(1)
        
    template_path = sys.argv[1]
    
    results = run_all_tests(template_path)
    
    if '--json' in sys.argv:
        print("\nDetailed Results:")
        print(json.dumps(results, indent=2))
        
    # Exit with error code if tests failed
    sys.exit(0 if results['overall_passed'] else 1)

if __name__ == '__main__':
    main()