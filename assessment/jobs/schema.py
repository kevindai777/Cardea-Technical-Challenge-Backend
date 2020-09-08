import graphene
from graphene_django import DjangoObjectType
from assessment.jobs.models import Job
from assessment.jobs.models import Category
from assessment.jobs.models import JobCategory

class JobType(DjangoObjectType):
    class Meta:
        model = Job
        fields = ("id", "title")

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name")

class JobCategoryType(DjangoObjectType):
    class Meta:
        model = JobCategory
        fields = ("id", "jobID", "categoryID")


class Query(graphene.ObjectType):
    jobs = graphene.List(JobType)
    job_by_id = graphene.Field(JobType, id = graphene.String())

    categories = graphene.List(CategoryType)
    category_by_id = graphene.Field(CategoryType, id = graphene.String())

    jobcategories = graphene.List(JobCategoryType)
    jobcategory_by_id = graphene.Field(JobCategoryType, id = graphene.String())

    def resolve_jobs(self, info, **kwargs):
        return Job.objects.all()

    def resolve_question_by_id(self, info, id):
        return Job.objects.get(pk=id)

    def resolve_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_category_by_id(self, info, id):
        return Category.objects.get(pk=id)

    def resolve_jobcategories(self, info, **kwargs):
        return JobCategory.objects.all()

    def resolve_jobcategory_by_id(self, info, **kwargs):
        return JobCategory.objects.get(pk=id)