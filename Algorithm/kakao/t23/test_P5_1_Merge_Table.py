from unittest import TestCase

from Algorithm.kakao.t23.P5_1_Merge_Table import P5_1_Merge_Table


class TestP5_1_Merge_Table(TestCase):
    def setUp(self):
        self.p5 = P5_1_Merge_Table()

    def test_solution(self):
        commands = ["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]
        expected = ["EMPTY", "group"]

        answer = self.p5.solution(commands)

        self.assertEquals(expected, answer)

    def test_solution2(self):
        commands = ["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]
        expected = ["d", "EMPTY"]

        answer = self.p5.solution(commands)

        self.assertEquals(expected, answer)


