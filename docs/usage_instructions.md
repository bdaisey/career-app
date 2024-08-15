## Django Admin Resume Editing

1. Create content in these Models listed on the lefthand side of the admin:

- Skills, Educations, Jobs (all linked to User)
- Bullets (linked to Job)

2. Create Resume and add previously created Skills, Educations, Jobs

3. To attach Bullets to a ResumeJob, edit ResumeJobs that were created in Step 2. (By editing already created ResumeJobs, the available Bullets will be filtered correctly. If adding a totally new Bullet from the popup window in this view, make sure to associate it with the current Job)

## Fixtures

### Dump existing database to fixture files.

There are only 2 apps with fixtures that we need to dump: Users and Resume. Simply run the following commands:

`python manage.py dumpdata auth.User --indent 4 --natural-primary --natural-foreign > fixtures/user_fixture.json`

`python manage.py dumpdata resume --indent 4 --natural-primary --natural-foreign > fixtures/resume_fixture.json`

### Load fixture files into fresh db.

Move or delete the existing database, run `migrate` to prep a fresh db, and load the fixtures. User fixtures must be loaded first because Resume fixtures reference Users. Run the following:

`python manage.py migrate`

`python manage.py loaddata fixtures/user_fixture.json fixtures/resume_fixture.json`
