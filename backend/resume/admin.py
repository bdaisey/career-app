from django.contrib import admin

from .models import Resume, PersonalInfo, Skill, ResumeSkill, Education, ResumeEducation, Job, Bullet, ResumeJob, ResumeJobBullet

class ResumeSkillInline(admin.TabularInline):
    model = ResumeSkill
    extra = 0

class ResumeEducationInline(admin.TabularInline):
    model = ResumeEducation
    extra = 0

class ResumeJobBulletInline(admin.TabularInline):
    model = ResumeJobBullet
    extra = 0

class ResumeJobInline(admin.TabularInline):
    model = ResumeJob
    extra = 0
    inlines = [ResumeJobBulletInline]

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'created_at', 'updated_at']
    inlines = [ResumeSkillInline, ResumeEducationInline, ResumeJobInline]

@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ['user', 'title']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['user', 'name']

@admin.register(ResumeSkill)
class ResumeSkillAdmin(admin.ModelAdmin):
    list_display = ['resume', 'skill', 'order', 'is_displayed']

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['user', 'degree_details']

    def degree_details(self, obj):
        return str(obj)

    degree_details.short_description = 'Education Info'

@admin.register(ResumeEducation)
class ResumeEducationAdmin(admin.ModelAdmin):
    list_display = ['resume', 'degree_details', 'order', 'is_displayed']

    def degree_details(self, obj):
        return str(obj.education)

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['user', 'job_details']

    def job_details(self, obj):
        return str(obj)

@admin.register(ResumeJob)
class ResumeJobAdmin(admin.ModelAdmin):
    list_display = ['user_details', 'resume_details', 'job_details']
    inlines = [ResumeJobBulletInline]

    def user_details(self, obj):
        return str(obj.resume.user)

    def resume_details(self, obj):
        return str(obj.resume)

    def job_details(self, obj):
        return str(obj.job)

@admin.register(Bullet)
class BulletAdmin(admin.ModelAdmin):
    list_display = ['user_details', 'job_details', 'content']

    def user_details(self, obj):
        return str(obj.job.user)

    def job_details(self, obj):
        return str(obj.job)

@admin.register(ResumeJobBullet)
class ResumeJobBulletAdmin(admin.ModelAdmin):
    list_display = ['user_details', 'resume_details', 'job_details', 'bullet_details']

    def user_details(self, obj):
        return str(obj.resume_job.resume.user)

    def resume_details(self, obj):
        return str(obj.resume_job.resume)

    def job_details(self, obj):
        return str(obj.resume_job.job)

    def bullet_details(self, obj):
        return str(obj.bullet)