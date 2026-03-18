---
name: template-deployer
description: Deploy, validate, and manage email templates with rollback capability. Use when dealing with template deployment crises, template validation failures, or requests to deploy/rollback templates. Triggers on "deploy template", "template crisis", "template deployment broken", "rollback template", or when template deployment paralysis occurs (Pattern 300 - Meta-Commentary Disease prevention).
---

# Template Deployer

Deploy and manage email templates with validation and rollback capabilities. Prevents template deployment paralysis through deterministic automation.

## Crisis Background

This skill addresses Pattern 300 (Meta-Commentary Disease) where 40+ agent votes on template deployment resulted in zero technical action. The Morning Brief template crisis took 25 minutes of coordination with no execution because deployment lacked automation.

## Core Operations

### 1. Template Validation
```bash
python scripts/validate_template.py <template_path>
```
- HTML structure validation
- Required section verification  
- Asset dependency checks
- Compatibility testing

### 2. Template Deployment
```bash
python scripts/deploy_template.py <template_path> --mode [staging|prod]
```
- Staging deployment with testing
- Production deployment with backup
- Rollback preparation
- Deployment verification

### 3. Rollback Management
```bash
python scripts/rollback_template.py --version [previous|specific]
```
- Immediate rollback to previous version
- Version-specific rollback
- Deployment history tracking

### 4. Integration Testing
```bash
python scripts/test_template.py <template_path>
```
- Render testing across email clients
- Link validation
- Asset accessibility verification
- Performance benchmarks

## Template Locations

- **Source templates:** `/root/.openclaw/workspace/templates/`
- **Deployed templates:** Target system endpoints (configured per environment)
- **Backup versions:** Automatic versioning with timestamps

## Environment Configuration

Templates deploy to different targets:
- **Staging:** Test environment for validation
- **Production:** Live email service integration
- **Backup:** Automatic backup before each deployment

## Usage Patterns

**Crisis Response:**
```bash
# Immediate crisis validation and deployment
python scripts/validate_template.py templates/brooke-demo-email.html
python scripts/deploy_template.py templates/brooke-demo-email.html --mode staging
python scripts/test_template.py templates/brooke-demo-email.html
python scripts/deploy_template.py templates/brooke-demo-email.html --mode prod
```

**Safe Deployment:**
```bash
# Standard deployment workflow
python scripts/deploy_template.py new-template.html --mode staging
# [manual verification]
python scripts/deploy_template.py new-template.html --mode prod
```

**Emergency Rollback:**
```bash
# Quick rollback when deployment fails
python scripts/rollback_template.py --version previous
```

## Pattern 299 Compliance

This skill follows atomic scope principles:
- Single responsibility: template deployment only
- Deterministic scripts prevent debate paralysis  
- Clear success/failure states
- No complex orchestration dependencies

## Integration Points

- **Resend API:** Production email template deployment
- **Hub Dashboard:** Template status monitoring
- **WhatsApp alerts:** Deployment success/failure notifications
- **Git tracking:** Template version control