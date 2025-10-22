# Contributing to AI Chatbot for School Queries

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## Ways to Contribute

1. **Report Bugs** 🐛
   - Use GitHub Issues
   - Include detailed description
   - Provide steps to reproduce
   - Include error messages and screenshots

2. **Suggest Features** 💡
   - Open a feature request issue
   - Explain the use case
   - Describe expected behavior

3. **Submit Code** 💻
   - Fix bugs
   - Add new features
   - Improve documentation
   - Optimize performance

4. **Improve Documentation** 📚
   - Fix typos
   - Add examples
   - Clarify instructions
   - Translate to other languages

## Getting Started

### 1. Fork the Repository

Click the "Fork" button at the top right of the repository page.

### 2. Clone Your Fork

```bash
git clone https://github.com/your-username/ai-chatbot-school-queries.git
cd ai-chatbot-school-queries
```

### 3. Create a Branch

```bash
git checkout -b feature/your-feature-name
```

Branch naming conventions:
- `feature/` - New features
- `bugfix/` - Bug fixes
- `docs/` - Documentation updates
- `refactor/` - Code refactoring

### 4. Make Your Changes

- Write clean, readable code
- Follow PEP 8 style guidelines
- Add comments for complex logic
- Update documentation as needed

### 5. Test Your Changes

```bash
# Run the application
streamlit run app.py

# Test various scenarios
# Verify no errors occur
```

### 6. Commit Your Changes

```bash
git add .
git commit -m "Description of changes"
```

Commit message format:
```
[Type]: Brief description

Detailed explanation if needed

Closes #issue_number (if applicable)
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Formatting
- `refactor`: Code restructuring
- `test`: Adding tests
- `chore`: Maintenance

### 7. Push to Your Fork

```bash
git push origin feature/your-feature-name
```

### 8. Create Pull Request

1. Go to the original repository
2. Click "New Pull Request"
3. Select your fork and branch
4. Fill in the PR template
5. Submit for review

## Code Standards

### Python Style Guide

- Follow PEP 8
- Use 4 spaces for indentation
- Maximum line length: 88 characters (Black formatter)
- Use descriptive variable names
- Add docstrings to functions

Example:
```python
def function_name(param1, param2):
    """
    Brief description of function.
    
    Args:
        param1 (type): Description
        param2 (type): Description
        
    Returns:
        type: Description
    """
    # Your code here
    return result
```

### File Organization

- Keep files focused and modular
- Use meaningful file names
- Organize imports (standard library, third-party, local)
- Add comments for complex logic

### Documentation

- Update README.md for new features
- Add inline comments for clarity
- Include usage examples
- Document configuration options

## Pull Request Guidelines

### PR Checklist

- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex code
- [ ] Documentation updated
- [ ] No new warnings or errors
- [ ] Tested on local machine
- [ ] Descriptive PR title and description

### PR Description Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
How the changes were tested

## Screenshots (if applicable)
Add screenshots here

## Related Issues
Fixes #(issue number)
```

## Reporting Bugs

### Bug Report Template

```markdown
**Describe the Bug**
Clear description of the bug

**To Reproduce**
Steps to reproduce:
1. Go to '...'
2. Click on '...'
3. See error

**Expected Behavior**
What should happen

**Screenshots**
If applicable

**Environment**
- OS: [e.g. Windows 10]
- Python Version: [e.g. 3.9]
- Streamlit Version: [e.g. 1.28.1]

**Additional Context**
Any other relevant information
```

## Feature Requests

### Feature Request Template

```markdown
**Feature Description**
Clear description of the feature

**Problem It Solves**
What problem does this solve?

**Proposed Solution**
How should it work?

**Alternatives Considered**
Other approaches you've thought about

**Additional Context**
Screenshots, mockups, examples
```

## Code Review Process

1. **Submission**: Create pull request
2. **Initial Review**: Maintainer checks basics
3. **Feedback**: Comments and suggestions
4. **Revisions**: Make requested changes
5. **Approval**: PR approved by maintainer
6. **Merge**: Code merged into main branch

## Community Guidelines

### Be Respectful

- Use welcoming language
- Respect different viewpoints
- Accept constructive criticism
- Focus on what's best for the community

### Be Collaborative

- Help others learn
- Share knowledge
- Give credit where due
- Be patient with newcomers

### Be Professional

- Keep discussions on-topic
- Avoid personal attacks
- Use appropriate language
- Respect privacy

## Questions?

- Check existing issues and discussions
- Read the documentation
- Ask in GitHub Discussions
- Contact maintainers

## Recognition

Contributors will be:
- Listed in README.md
- Credited in release notes
- Recognized in the community

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing! 🎉

