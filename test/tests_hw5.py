import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from hw5 import Patient, Card, Deck, Triangle, Rectangle, Circle

# Tests for Patient class
def test_patient_has_covid_with_positive_test():
    patient = Patient("John Doe", ["fever", "cough"])
    patient.add_test("covid", True)
    assert patient.has_covid() == 0.99, "Expected probability to be 0.99 for a positive test"

def test_patient_has_covid_with_negative_test():
    patient = Patient("John Doe", ["fever", "cough"])
    patient.add_test("covid", False)
    assert patient.has_covid() == 0.01, "Expected probability to be 0.01 for a negative test"

def test_patient_has_covid_based_on_symptoms():
    patient = Patient("Jane Doe", ["fever", "cough", "anosmia"])
    assert patient.has_covid() == 0.35, "Expected probability based on symptoms to be 0.35"

def test_patient_has_covid_no_symptoms():
    patient = Patient("Jake Doe", [])
    assert patient.has_covid() == 0.05, "Expected base probability to be 0.05 for no symptoms"

def test_patient_has_covid_partial_symptoms():
    patient = Patient("Jim Doe", ["fever"])
    assert patient.has_covid() == 0.15, "Expected probability based on one symptom to be 0.15"


# Tests for Deck and Card classes
def test_deck_initialization():
    deck = Deck()
    assert len(deck.cards) == 52, "Expected 52 cards in a new deck"

def test_deck_shuffle():
    deck = Deck()
    cards_before_shuffle = deck.cards[:]
    deck.shuffle()
    assert deck.cards != cards_before_shuffle, "Expected deck to be shuffled"

def test_deck_draw():
    deck = Deck()
    deck.shuffle()
    initial_length = len(deck.cards)
    drawn_card = deck.draw()
    assert len(deck.cards) == initial_length - 1, "Expected one less card after drawing"
    assert isinstance(drawn_card, Card), "Expected drawn card to be a Card instance"


# Tests for PlaneFigure subclasses (Triangle, Rectangle, Circle)
def test_triangle_perimeter():
    triangle = Triangle(base=3, c1=4, c2=5, h=2)
    assert triangle.compute_perimeter() == 12, "Expected perimeter to be 12"

def test_triangle_surface():
    triangle = Triangle(base=3, c1=4, c2=5, h=2)
    assert triangle.compute_surface() == 3.0, "Expected surface area to be 3.0"

def test_rectangle_perimeter():
    rectangle = Rectangle(a=3, b=4)
    assert rectangle.compute_perimeter() == 14, "Expected perimeter to be 14"

def test_rectangle_surface():
    rectangle = Rectangle(a=3, b=4)
    assert rectangle.compute_surface() == 12, "Expected surface area to be 12"

def test_circle_perimeter():
    circle = Circle(radius=3)
    assert round(circle.compute_perimeter(), 2) == 18.85, "Expected perimeter to be approximately 18.85"

def test_circle_surface():
    circle = Circle(radius=3)
    assert round(circle.compute_surface(), 2) == 28.27, "Expected surface area to be approximately 28.27"
