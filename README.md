# End-to-End Invoice Processing

## Overview
This UiPath automation project implements an end-to-end invoice processing system that automates the entire workflow from email receipt to data extraction and reporting. The system includes spam filtering, intelligent document processing, and automated reporting capabilities.

## Features
- Gmail integration for invoice email retrieval
- Spam detection and filtering using Python
- Automated invoice processing using Document Understanding
- Data extraction and consolidation to Excel
- Automated daily report generation and email distribution

## Technical Requirements

### UiPath Dependencies
- UiPath Studio: v22.2.36.24289-preview
- Document Understanding ML Activities: v1.9.1
- Excel Activities: v2.11.4
- Intelligent OCR Activities: v5.0.2
- Mail Activities: v1.12.3
- System Activities: v21.10.4
- Testing Activities: v1.4.6
- UI Automation Activities: v21.10.5

### Project Configuration
- Framework: Legacy
- Studio Version: 21.10.5.0
- Project Version: 1.0.0
- Expression Language: VisualBasic

## Project Structure
- `Main.xaml`: Primary workflow entry point
- Test Cases:
  - GeneralTestCase.xaml
  - GetTransactionDataTestCase.xaml
  - InitAllApplicationsTestCase.xaml
  - InitAllSettingsTestCase.xaml
  - MainTestCase.xaml
  - ProcessTestCase.xaml
  - WorkflowTestCaseTemplate.xaml

## Runtime Configuration
- Execution Type: Workflow
- Attended/Unattended: Unattended
- User Interaction Required: Yes
- Persistence Support: No
- Auto-dispose: Disabled
- .NET Framework Lazy Loading: Disabled

## Security Notes
- Private data and password fields are automatically excluded from logging
- Original XAML is not included in library output

## Getting Started

### Prerequisites
1. UiPath Studio (version 22.2.36 or compatible)
2. Gmail account with appropriate permissions
3. Python environment for spam detection

### Installation
1. Clone the repository
2. Open the project in UiPath Studio
3. Restore all NuGet dependencies
4. Configure email settings in the project configuration
5. Set up the Python environment for spam detection

### Usage
1. The automation will monitor the configured Gmail account
2. New emails with invoices will be processed through spam detection
3. Valid invoices will be processed using Document Understanding
4. Extracted data will be consolidated into Excel
5. A daily report will be generated and emailed to configured recipients

## Testing
The project includes comprehensive test cases covering:
- General functionality
- Transaction data processing
- Application initialization
- Settings configuration
- Main workflow execution
- Process-specific scenarios

Run the test cases through UiPath Test Suite to ensure proper functionality.

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Reques
