import graphene
from graphene_django import DjangoObjectType
from assessment.jobs.models import Example as ExampleModel
from assessment.jobs.models import Job 
from assessment.jobs.models import Category
from assessment.jobs.models import JobCategory


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

class CreateCategory(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()

    class Arguments:
        name = graphene.String()
    
    def mutate(self, info, name):
        category = Category(name=name)
        category.save()

        return CreateCategory(
            id=category.id,
            name=category.name,
        )




class JobType(DjangoObjectType):
    class Meta:
        model = Job

class CreateJob(graphene.Mutation):
    id = graphene.Int()
    title = graphene.String()

    class Arguments:
        title = graphene.String()

    def mutate(self, info, title):
        job = Job(title=title)
        job.save()

        return CreateJob(
            id=job.id,
            title=job.title,
        )




class JobCategoryType(DjangoObjectType):
    class Meta:
        model = JobCategory

class CreateJobCategory(graphene.Mutation):
    id = graphene.Int()
    jobID = graphene.Int()
    categoryID = graphene.Int()

    class Arguments:
        jobID = graphene.Int()
        categoryID = graphene.Int()

    def mutate(self, info, jobID, categoryID):
        jobcategory = JobCategory(jobID=jobID, categoryID=categoryID)
        jobcategory.save()

        return CreateJobCategory(
            id=jobcategory.id,
            jobID=jobcategory.jobID,
            categoryID=jobcategory.categoryID,
        )






class Query(graphene.ObjectType):
    categories = graphene.List(CategoryType)
    jobs = graphene.List(JobType)
    jobcategories = graphene.List(JobCategoryType)

    def resolve_categories(self, info):
        return Category.objects.all()
    
    def resolve_jobs(self, info):
        return Job.objects.all()
    
    def resolve_jobcategories(self, info):
        return JobCategory.objects.all()

class Mutation(graphene.ObjectType):
    create_job = CreateJob.Field()
    create_category = CreateCategory.Field()
    create_jobcategory = CreateJobCategory.Field()