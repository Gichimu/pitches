from app.models import Pitch
from app import db
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
        self.test_pitch = Pitch(id=10, pitch_pic_loc="photos/animal.jpg", pitch_body="test pitch body", user_id=1)

        

    def test_isInstance(self):
        '''
        Method to check if the initialized object is an instance of the class pitch
        '''
        self.assertTrue(isinstance(self.test_pitch, Pitch))

    
    def test_save_pitch(self):
        test_pitch = Pitch(id=23, pitch_pic_loc="photos/animal.jpg", pitch_body="lorem ipsum dolor asimet", user_id=1)
        Pitch.save_pitch(test_pitch)
        pitch = Pitch.query.filter_by(id = test_pitch.id).first()
        self.assertEqual(pitch.pitch_body, "lorem ipsum dolor asimet")
        


    def test_get_pitches(self):
        pitches = Pitch.query.filter_by(user_id = 1).all()
        self.assertIsNotNone(pitches)

    def tearDown(self):
        '''
        Method to clean up all the initializations done on each test run
        '''
        pass
        

    