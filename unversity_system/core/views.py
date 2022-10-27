from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Discipline, StudentGroup, StudyingDirection


class AddStudentToGroupView(APIView):
    def post(self, request):
        pass