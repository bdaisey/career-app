from django.contrib.auth.models import User
from django.db import models

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resumes')
    title = models.CharField(max_length=200, help_text="Title of the resume, e.g. 'Software Dev at Startup Resume'")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.title}"


class PersonalInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='personal_info_entries')
    title = models.CharField(max_length=200, help_text="Description of info, e.g. 'DC Rental Rowhouse'")
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=300, blank=True)
    linkedin = models.URLField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.full_name

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='education_entries')
    school_name = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.degree} in {self.field_of_study} from {self.school_name}"

class ResumeEducation(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    education = models.ForeignKey(Education, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()
    is_displayed = models.BooleanField(default=True)

    class Meta:
        unique_together = ('resume', 'education')
        ordering = ['order']

class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ResumeSkill(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()
    is_displayed = models.BooleanField(default=True)

    class Meta:
        unique_together = ('resume', 'skill')
        ordering = ['order']

class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs')
    job_title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"


class Bullet(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.content


class ResumeJob(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()

    class Meta:
        unique_together = ('resume', 'job')
        ordering = ['order']

    def __str__(self):
        return f"{self.resume} - {self.job}"


class ResumeJobBullet(models.Model):
    resume_job = models.ForeignKey(ResumeJob, on_delete=models.CASCADE)
    bullet = models.ForeignKey(Bullet, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()
    is_displayed = models.BooleanField(default=True)

    class Meta:
        unique_together = ('resume_job', 'bullet')
        ordering = ['order']