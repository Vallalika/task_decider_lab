import unittest
from src.task import *
from src.task_decider import *

class TaskTest(unittest.TestCase):

    def setUp(self):
        self.wash_dishes = Task("Wash the dishes", 30)
        self.cook_dinner = Task("Cook dinner", 60)
        self.clean_windows = Task("Clean windows", 45)
        self.wash_clothes = Task("Wash clothes", 120)
        self.do_ironing = Task("Do ironing", 120)

    
    # @unittest.skip
    def test_task_set_up(self):
        self.assertEqual("Wash the dishes",self.wash_dishes.description)
        self.assertEqual(30,self.wash_dishes.duration)

    # @unittest.skip
    def test_dishes_over_dinner(self):
        self.assertEqual("Wash the dishes", get_preferred_option(self.wash_dishes, self.cook_dinner))
        self.assertEqual("Wash the dishes", get_preferred_option(self.cook_dinner, self.wash_dishes))
    
    # @unittest.skip
    def test_dinner_over_windows(self):
        self.assertEqual("Cook dinner", get_preferred_option(self.cook_dinner, self.clean_windows))
        self.assertEqual("Cook dinner", get_preferred_option(self.clean_windows, self.cook_dinner))
    
    # @unittest.skip
    def test_windows_over_dishes(self):
        self.assertEqual("Clean windows", get_preferred_option(self.clean_windows, self.wash_dishes))
        self.assertEqual("Clean windows", get_preferred_option(self.wash_dishes, self.clean_windows))
    
    @unittest.skip
    def test_dishes_over_clothes(self):
        self.assertEqual("Wash the dishes", get_preferred_option(self.wash_dishes, self.wash_clothes))
        self.assertEqual("Clean windows", get_preferred_option(self.wash_clothes, self.wash_dishes))
    
    @unittest.skip
    def test_dinner_over_ironing(self):
        self.assertEqual("Cook dinner", get_preferred_option(self.cook_dinner, self.do_ironing))
        self.assertEqual("Cook dinner", get_preferred_option(self.do_ironing, self.cook_dinner))
    
    @unittest.skip
    def test_windows_over_ironing(self):
        self.assertEqual("Clean windows", get_preferred_option(self.clean_windows, self.do_ironing))
        self.assertEqual("Clean windows", get_preferred_option(self.do_ironing, self.clean_windows))
    
