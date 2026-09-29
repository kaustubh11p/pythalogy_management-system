# Problem Statement

## Title
Pathology Lab Management System

## Background
Small pathology laboratories often handle patient records, test bookings, sample tracking, reports, and billing on paper or in scattered spreadsheets. This leads to lost records, mismatched reports, billing errors, and no clear view of where a patient's sample is in the process.

## Problem
Design and implement a simple software system that lets lab staff manage the complete lifecycle of a diagnostic test in one place — from patient registration to final bill — with a clear status for every booking.

## Objectives
1. Register patients and store their details (name, age, gender, contact).
2. Maintain a catalog of available tests with fixed prices.
3. Allow a test to be booked for a registered patient.
4. Track each booking through defined stages: **Sample Pending → Sample Collected → Report Ready**.
5. Prevent out-of-order operations (e.g. no report before the sample is collected).
6. Record the test result and display the report.
7. Generate an itemised bill with a total for a patient's bookings.

## Scope
**In scope**
- Console (text menu) interface
- In-memory storage during a single run
- Six predefined tests
- Single-user operation

**Out of scope**
- Database or file persistence
- Graphical or web interface
- Authentication / multiple user roles
- Payment processing, online report delivery, reference ranges

## Inputs
- Patient details (name, age, gender, contact)
- Patient ID, test ID, booking ID
- Test result text

## Outputs
- Confirmation messages (patient registered, test booked, sample collected, report generated)
- List of patients and bookings
- Test catalog
- Test report (patient, test, result)
- Itemised bill with total

## Constraints
- Python 3, standard library only
- Modular design: separate modules for patients, tests, bookings, billing
- Runs in a terminal

## Expected Outcome
A working menu-driven program that guides lab staff through registration, booking, sample collection, reporting, and billing, and enforces the correct order of steps.
