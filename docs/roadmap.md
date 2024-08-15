# Project Roadmap

## Django backend, admin, basic frontend setup

- [x] Create models - Resume, PersonalInfo, Job, Bullet, Education, Skill
- [x] Create migrations and migrate
- [x] Setup admin and create a test resume
- [x] Django template to display a resume
- [ ] Add to resume models to allow natural keys during fixture dump/load
- [ ] Add 'personal_info' field to resume model and admin
- [ ] Dump resume models and users
- [ ] Switch to new db and load resume models and users
- [ ] Script to load fixtures in correct order (dump too?)
- [ ] Write usage instructions for fixtures, include how to add new bullets

## DRF setup

- [ ] Add DRF and serializers
- [ ] Install docs for API
- [ ] Test API
- [ ] Write template to display single resume using API instead of db

## Project enhancements

- [ ] Add linters/formatters
- [ ] Add pre-commit hooks
- [ ] Research other enhancements to add

## React basic frontend

- [ ] Add a dropdown to select a resume display its content
- [ ] Add drag and drop reorder of sections Job, Education, Skill
- [ ] Add drag and drop reorder of Bullets within Job
- [ ] Write exporter for a text version

## Share local version

- [ ] Write a script to create the django project, migrate, load test resumes, and run

## Functionality to create/edit/delete content from frontend

## Set up frontend for user login

## Create basic PDF exporter

## Deploy on AWS
