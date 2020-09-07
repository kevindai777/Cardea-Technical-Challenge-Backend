import graphene
from graphene_django import DjangoObjectType
import assessment.jobs.schema
import assessment.jobs.mutations
from assessment.jobs.models import UserModel
from assessment.jobs.models import Job 
from assessment.jobs.models import Category
from assessment.jobs.models import JobCategory

class UserType(DjangoObjectType):
    class Meta:
        model = UserModel

class CreateUser(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    last_name = graphene.String()

    class Arguments:
        last_name = graphene.String()
        name = graphene.String()

    def mutate(self, info, name, last_name):
        user = UserModel(name=name, last_name=last_name)
        user.save()

        return CreateUser(
            id=user.id,
            name=user.name,
            last_name=user.last_name,
        )




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
    create_jobcategory = CreateJobCategory.Field()


# class Query(
#     assessment.jobs.schema.Query,
# ):
#     pass


# class Mutation(
#     assessment.jobs.mutations.Mutation,
# ):
#     pass


schema = graphene.Schema(
    query=Query, mutation=Mutation
)