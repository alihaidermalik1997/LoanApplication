# Loan Application Project

This project is a test given by affinity.

## Getting Started

Follow the instructions below to set up and run the project locally.

### Prerequisites

- Python 3.x
- Git

### Installation

1. Clone the project using Git:

   ```shell
   git clone git@github.com:alihaidermalik1997/LoanApplication.git
   
1. Create a Python virtual environment:

   ```shell
   python3 -m venv myenv
   
1. Activate the environment:

   ```shell
   source myenv/bin/activate

1. Navigate to the project's main directory:

   ```shell
   cd LoanApplication/

1. Install the project dependencies:

   ```shell
   pip install -r requirements.txt

1. Run the development server:

   ```shell
   ./manage.py runserver

### Running the Cron Job

To run the cron job that notifies users before two days of the due date, use the following command:
   ```shell
   ./manage.py notify_users
   ```   
### API Postman Collection
A Postman collection containing the API endpoints and sample requests is provided in the repository.
