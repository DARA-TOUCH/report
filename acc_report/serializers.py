from rest_framework import serializers

class FileUploadSerializer(serializers.Serializer):
    sad_file = serializers.FileField()
    budget_file = serializers.FileField()


class DowloadAccReportFormSerializer(serializers.Serializer):
    pass
    