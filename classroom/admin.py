from django.contrib import admin
from django.utils.html import format_html

from .models import User, Subject, Quiz, Question, Answer, Student, TakenQuiz, StudentAnswer
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_('Additional Fields'), {'fields': ('is_student', 'is_teacher')}),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'first_name', 'last_name'),
        }),
    )


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'display_html_badge')

    def display_html_badge(self, obj):
        return format_html(obj.get_html_badge())

    display_html_badge.short_description = 'Badge'
    display_html_badge.allow_tags = True

    # def get_html_badge(self, obj):
    #     return format_html('<span class="badge badge-primary" style="background-color: {}">{}</span>',
    #                        obj.color, obj.name)


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'subject')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'quiz')


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text', 'question', 'is_correct')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_interests')

    def get_interests(self, obj):
        return ", ".join([str(interest) for interest in obj.interests.all()])

    get_interests.short_description = 'Interests'


@admin.register(TakenQuiz)
class TakenQuizAdmin(admin.ModelAdmin):
    list_display = ('student', 'quiz', 'score', 'date')


@admin.register(StudentAnswer)
class StudentAnswerAdmin(admin.ModelAdmin):
    list_display = ('student', 'answer')
