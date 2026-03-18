---
name: template-deployer
description: Deploy email templates to production with validation and rollback capability. Use when user says "deploy template" or during template crises like Pattern 281-282.
---

# Template Deployer

Deploy email templates to production with validation, staging, and rollback capability.

## When to Use

- User says "deploy template" or "template crisis"
- Morning Brief template issues (Pattern 281-282)
- Template exists but deployment pipeline is blocked
- Need to rollback a template deployment
- Template validation before production

**Trigger Phrases:**
- "deploy template"
- "template crisis" 
- "brooke template"
- "morning brief template"
- "rollback template"

## Prerequisites

- Hub API access (`HUB_API_KEY`)
- Template files in `templates/` directory
- Production deployment permissions

## Usage

### Deploy Template
```bash
python3 ~/.openclaw/workspace/skills/template-deployer/scripts/deploy_template.py \
  --template brooke-demo-email.html \
  --environment production \
  --validate
```

### Stage Template (Test First)
```bash
python3 ~/.openclaw/workspace/skills/template-deployer/scripts/deploy_template.py \
  --template brooke-demo-email.html \
  --environment staging \
  --validate
```

### Rollback Template
```bash
python3 ~/.openclaw/workspace/skills/template-deployer/scripts/deploy_template.py \
  --rollback \
  --environment production
```

### Validate Template Only
```bash
python3 ~/.openclaw/workspace/skills/template-deployer/scripts/validate_template.py \
  --template brooke-demo-email.html
```

## Template Crisis Context

**Pattern 281-282: Template-Pipeline Paradox**
- 600-line brooke-demo-email.html EXISTS and is production-ready
- 40+ agent votes and 20+ hours of debate generated zero deployments
- Template is DONE; deployment pipeline was the blocker
- This skill bridges template→pipeline gap with atomic deployment capability

**Evidence from Sessions:**
- 2026-03-17: Template crisis consumed 25min of unanimous agent response
- brooke-demo-email.html: 600+ lines, production-ready, Brooke Theme compliant
- Multiple escalations for "Deploy template" with no execution pathway

## Features

- ✅ Template validation (HTML, CSS, responsive design)
- ✅ Staging deployment for testing
- ✅ Production deployment with confirmation
- ✅ Automatic rollback capability
- ✅ Template comparison (current vs new)
- ✅ Deployment history tracking
- ✅ Hub API integration for live templates

## Template Validation Checks

1. **HTML Structure**: Valid HTML5, proper email-friendly tags
2. **CSS Compatibility**: Inline CSS, email client compatibility  
3. **Responsive Design**: Mobile-friendly layout
4. **Variables**: Template variables properly formatted
5. **Content**: Required sections present (header, body, footer)
6. **Brooke Theme**: Color palette compliance (cream/sage/copper)

## Deployment Flow

```
Template File → Validate → Stage → Test → Deploy → Confirm → Rollback Available
```

1. **Validation**: Check HTML structure, CSS, responsiveness
2. **Staging**: Deploy to staging environment for testing
3. **Testing**: Send test emails, verify rendering
4. **Production**: Deploy to live environment
5. **Confirmation**: Verify production deployment success
6. **Rollback**: Previous version preserved for emergency rollback

## Examples

### Deploy Brooke Template (Crisis Solution)
```bash
# The template crisis fix - atomic 30-minute execution
python3 ~/.openclaw/workspace/skills/template-deployer/scripts/deploy_template.py \
  --template brooke-demo-email.html \
  --environment production \
  --validate \
  --confirm
```

### Emergency Rollback
```bash
# If new template causes issues
python3 ~/.openclaw/workspace/skills/template-deployer/scripts/deploy_template.py \
  --rollback \
  --environment production \
  --reason "Template rendering issues on mobile"
```

### Test New Template
```bash
# Safe testing workflow
python3 ~/.openclaw/workspace/skills/template-deployer/scripts/deploy_template.py \
  --template new-template.html \
  --environment staging \
  --validate \
  --test-email joey@photobarchicago.com
```

## Files

- `scripts/deploy_template.py` - Main deployment script
- `scripts/validate_template.py` - Template validation
- `scripts/test_template.py` - Template testing
- `templates/` - Template directory (workspace-level)

## Implementation Notes

**Atomic Scope (Pattern 299):**
- Single command deploys a template
- 30-minute execution window
- Clear success/failure states
- No complex orchestration required

**Crisis Response:**
- Solves 600-line brooke-demo-email.html deployment gap
- Ends 20+ hour template debate loops
- Enables launch week template deployment

**Integration:**
- Hub API for live template updates
- Railway deployment integration  
- WhatsApp alerts for deployment status
- Git tracking for template versions