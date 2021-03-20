from django.test import TestCase, Client

from .models import Student


# Create your tests here.

class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(
            name="tian",
            sex=1,
            email="333355@qq.com",
            profession="程序员",
            qq="3333333",
            phone="1345555990",
        )

    def test_create_and_sex_show(self):
        student = Student.objects.create(
            name="xiang",
            sex=1,
            email="xiangxiang@123.com",
            profession="文员",
            qq="55667788",
            phone="1380009900",
        )
        self.assertEqual(student.get_sex_display(), "男", "性别字段内容跟展示不一致")

    def test_filter(self):
        Student.objects.create(
            name="tianxiang",
            sex=1,
            email="lilimli@qq.com",
            profession="销售",
            qq="666777",
            phone="139099000",
        )
        name = "tian"
        students = Student.objects.filter(name=name)
        self.assertEqual(students.count(), 1, "应该只存在一个名称为{0}的记录".format(name))

    # 视图层测试
    def test_get_index(self):
        """
        测试index首页可用性
        :return:
        """
        client = Client()
        response = client.get("/")
        self.assertEqual(response.status_code, 200, "status code must be 200")

    def test_post_student(self):
        """
        提交数据进行测试
        :return:
        """
        client = Client()
        data = dict(
            name='test_for_post',
            sex=1,
            email='333333@qq.com',
            profession="文员",
            qq="33333",
            phone="33555",
        )
        response = client.post("/", data)
        self.assertEqual(response.status_code, 302, 'status code must be 302')

        response = client.get("/")
        self.assertTrue(b'test_for_post' in response.content,
                        "response content must contain 'test_for_post'"
                        )
