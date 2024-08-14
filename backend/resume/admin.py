from django.contrib import admin

from .models import Resume, PersonalInfo, Skill, ResumeSkill, Education, ResumeEducation, Job, Bullet, ResumeJob, ResumeJobBullet


class FilterByResumeUserMixin:
    def get_form(self, request, obj=None, **kwargs):
        request._obj_ = obj
        return super().get_form(request, obj, **kwargs)

    def filter_queryset_by_resume_user(self, db_field, request, kwargs):
        if request._obj_ is not None:
            user = request._obj_.user
            model_map = {
                'job': Job,
                'skill': Skill,
                'education': Education,
            }
            if db_field.name in model_map:
                kwargs["queryset"] = model_map[db_field.name].objects.filter(user=user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        self.filter_queryset_by_resume_user(db_field, request, kwargs)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class FilterByResumeJobMixin:
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "bullet":
            if hasattr(request, '_obj_') and request._obj_ is not None:
                resume_job = request._obj_
                job = resume_job.job
                kwargs["queryset"] = Bullet.objects.filter(job=job)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class ResumeSkillInline(FilterByResumeUserMixin, admin.TabularInline):
    model = ResumeSkill
    extra = 0

class ResumeEducationInline(FilterByResumeUserMixin, admin.TabularInline):
    model = ResumeEducation
    extra = 0

class ResumeJobBulletInline(FilterByResumeJobMixin, admin.TabularInline):
    model = ResumeJobBullet
    extra = 0

    def get_formset(self, request, obj=None, **kwargs):
        request._obj_ = obj
        return super().get_formset(request, obj, **kwargs)

class ResumeJobInline(FilterByResumeUserMixin, admin.TabularInline):
    model = ResumeJob
    extra = 0
    inlines = [ResumeJobBulletInline]

@admin.register(Resume)
class ResumeAdmin(FilterByResumeUserMixin, admin.ModelAdmin):
    list_display = ['user', 'title', 'created_at', 'updated_at']
    list_filter = ['user']
    search_fields = ['title', 'user__username']
    ordering = ['user', 'title']
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
    list_filter = ['resume', 'skill', 'is_displayed']
    search_fields = ['resume__title', 'skill__name']
    ordering = ['resume', 'order']

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['user', 'degree_details']

    def degree_details(self, obj):
        return str(obj)

    degree_details.short_description = 'Education Info'

@admin.register(ResumeEducation)
class ResumeEducationAdmin(admin.ModelAdmin):
    list_display = ['resume', 'degree_details', 'order', 'is_displayed']
    list_filter = ['resume', 'education', 'is_displayed']
    search_fields = ['resume__title']
    ordering = ['resume', 'order']

    def degree_details(self, obj):
        return str(obj.education)

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['user', 'job_details']

    def job_details(self, obj):
        return str(obj)

@admin.register(ResumeJob)
class ResumeJobAdmin(admin.ModelAdmin):
    list_display = ['user_details', 'resume_details', 'job_details', 'order']
    list_filter = ['resume', 'job']
    search_fields = ['resume__title', 'job__title']
    ordering = ['resume', 'order']
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
class ResumeJobBulletAdmin(FilterByResumeJobMixin, admin.ModelAdmin):
    list_display = ['user_details', 'resume_details', 'job_details', 'bullet_details', 'order', 'is_displayed']
    list_filter = ['resume_job__resume', 'resume_job__job', 'is_displayed']
    search_fields = ['resume_job__resume__title', 'resume_job__job__title', 'bullet__content']
    ordering = ['resume_job__resume', 'resume_job__order', 'order']

    def user_details(self, obj):
        return str(obj.resume_job.resume.user)

    def resume_details(self, obj):
        return str(obj.resume_job.resume)

    def job_details(self, obj):
        return str(obj.resume_job.job)

    def bullet_details(self, obj):
        return str(obj.bullet)

    def get_form(self, request, obj=None, **kwargs):
        if obj:
            request._resume_job_ = obj.resume_job
        return super().get_form(request, obj, **kwargs)