import uuid

from django.contrib.auth.models import User
from django.db import models


class PersonalInfoManager(models.Manager):
    def get_by_natural_key(self, username, title):
        return self.get(user__username=username, title=title)

class PersonalInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='personal_info_entries')
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=200, help_text="Description of info, e.g. 'DC Rental Rowhouse'")
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=300, blank=True)
    linkedin = models.URLField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'title'], name='unique_user_personalinfotitle')
        ]

    def natural_key(self):
        return (self.user.username, self.title)

    objects = PersonalInfoManager()

    def __str__(self):
        return f"{self.full_name} - {self.title}"

class ResumeManager(models.Manager):
    def get_by_natural_key(self, username, title ):
        return self.get(user__username=username, title=title)

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resumes')
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, related_name='resumes')
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=200, help_text="Title of the resume, e.g. 'Software Dev at Startup Resume'")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'title'], name='unique_user_resumetitle')
        ]

    def natural_key(self):
        return (self.user.username, self.title)

    objects = ResumeManager()

    def __str__(self):
        return f"{self.user.username} - {self.title}"

class EducationManager(models.Manager):
    def get_by_natural_key(self, username, school_name, degree, field_of_study ):
        return self.get(user__username=username, school_name=school_name, degree=degree, field_of_study=field_of_study)

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='education_entries')
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    school_name = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField(blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'school_name', 'degree', 'field_of_study'], name='unique_user_school_degree_field')
        ]

    def natural_key(self):
        return (self.user.username, self.school_name, self.degree, self.field_of_study)

    objects = EducationManager()

    def __str__(self):
        return f"{self.degree} in {self.field_of_study} from {self.school_name}"

class ResumeEducationManager(models.Manager):
    def get_by_natural_key(self, resume_uuid, education_uuid):
        return self.get(resume__uuid=resume_uuid, education__uuid=education_uuid)

class ResumeEducation(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    education = models.ForeignKey(Education, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()
    is_displayed = models.BooleanField(default=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['resume', 'education'], name='unique_resume_education')
        ]
        ordering = ['order']

    def natural_key(self):
        return (self.resume.uuid, self.education.uuid)

    objects = ResumeEducationManager()

class SkillManager(models.Manager):
    def get_by_natural_key(self, username, name):
        return self.get(user__username=username, name=name)

class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skills')
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'name'], name='unique_user_name')
        ]

    def natural_key(self):
        return (self.user.username, self.name)

    objects = SkillManager()

    def __str__(self):
        return self.name

class ResumeSkillManager(models.Manager):
    def get_by_natural_key(self, resume_uuid, skill_uuid ):
        return self.get(resume__uuid=resume_uuid, skill__uuid=skill_uuid)

class ResumeSkill(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()
    is_displayed = models.BooleanField(default=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['resume', 'skill'], name='unique_resume_skill')
        ]
        ordering = ['order']

    def natural_key(self):
        return (self.resume.uuid, self.skill.uuid)

    objects = ResumeSkillManager()

class JobManager(models.Manager):
    def get_by_natural_key(self, username, job_title, company_name ):
        return self.get(user__username=username, job_title=job_title, company_name=company_name)

class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs')
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    job_title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField(blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'job_title', 'company_name'], name='unique_user_job_title_company')
        ]

    def natural_key(self):
        return (self.user.username, self.job_title, self.company_name)

    objects = JobManager()

    def __str__(self):
        return f"{self.job_title} at {self.company_name} ({self.user})"

class BulletManager(models.Manager):
    def get_by_natural_key(self, job_uuid, content):
        return self.get(job__uuid=job_uuid, content=content)

class Bullet(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    content = models.TextField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['job', 'content'], name='unique_job_content')
        ]

    def natural_key(self):
        return (self.job.uuid, self.content)

    objects = BulletManager()

    def __str__(self):
        return self.content

class ResumeJobManager(models.Manager):
    def get_by_natural_key(self, resume_uuid, job_uuid ):
        return self.get(resume__uuid=resume_uuid, job__uuid=job_uuid)

class ResumeJob(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['resume', 'job'], name='unique_resume_job')
        ]
        ordering = ['order']

    def natural_key(self):
        return (self.resume.uuid, self.job.uuid)

    objects = ResumeJobManager()

    def __str__(self):
        return f"{self.resume} - {self.job}"

class ResumeJobBulletManager(models.Manager):
    def get_by_natural_key(self, resume_job, bullet_uuid ):
        return self.get(resume_job=resume_job, bullet__uuid=bullet_uuid)

class ResumeJobBullet(models.Model):
    resume_job = models.ForeignKey(ResumeJob, on_delete=models.CASCADE)
    bullet = models.ForeignKey(Bullet, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()
    is_displayed = models.BooleanField(default=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['resume_job', 'bullet'], name='unique_resume_job_bullet')
        ]
        ordering = ['order']

    def natural_key(self):
        return (self.resume_job, self.bullet.uuid)

    objects = ResumeJobBulletManager()
