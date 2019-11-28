from app.models import Pitch
import unittest


class test_pitch(unittest.TestCase):
    '''
    Test class that defines tests for the Pitch model

    Args:
        unittest.TestCase: test superclass from which this class inherits
    '''

    def setUp(self):
        '''
        Default function that runs on each test run
        '''
        self.test_pitch = Pitch(id=1, pitch_pic_loc="photos/animal.jpg", pitch_body="test pitch body", user_id=1)

    def tearDown(self):
        '''
        Method to clean up all the initializations done on each test run
        '''
        pass

    def test_isInstance(self):
        '''
        Method to check if the initialized object is an instance of the class pitch
        '''
        self.assertTrue(isinstance(self.test_pitch, Pitch))

    
    def test_save_pitch(self):
        Pitch.save_pitch(self.test_pitch)
        pitch = Pitch.query.filter_by(id = self.test_pitch.id).first()
        self.assertEqual(pitch.pitch_body, self.test_pitch.pitch_body)

        

    