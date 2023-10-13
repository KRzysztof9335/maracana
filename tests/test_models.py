"Tests for models"
import pytest
import lib.models

def test_participant_class():
    assert "HOME" == lib.models.Participant.HOME.name
    assert "AWAY" == lib.models.Participant.AWAY.name


# =================================================================================================

def test_prediction_creation_correct_probability():
    inst = lib.models.Prediction(lib.models.PredictionEvents.CARD_RED, 70.7)

    assert inst.name.value == "card_red"
    assert inst.probability == 70.7
    assert inst.course == 1.1
    assert inst.expected
    assert inst.real == None
    assert inst.guessed == None


def test_prediction_creation_wrong_probability_too_low():
    with pytest.raises(ValueError):
        lib.models.Prediction(lib.models.PredictionEvents.CARD_RED, -0.1)


def test_prediction_creation_wrong_probability_too_big():
    with pytest.raises(ValueError):
        lib.models.Prediction(lib.models.PredictionEvents.CARD_RED, 100.01)


def test_prediction_update_guessed():
    inst = lib.models.Prediction(lib.models.PredictionEvents.CARD_RED, 70.7, expected=False)
    assert not inst.expected
    assert inst.real == None
    assert inst.guessed == None

    inst.update_prediction(False)

    assert not inst.real
    assert inst.guessed


def test_prediction_update_not_guessed():
    inst = lib.models.Prediction(lib.models.PredictionEvents.CARD_RED, 70.7, expected=False)
    assert not inst.expected
    assert inst.real == None
    assert inst.guessed == None

    inst.update_prediction(True)

    assert inst.real
    assert not inst.guessed

# =================================================================================================


def test_match_creation():
    inst = lib.models.Match("2022", "C", "L", "HT", "AT")

    assert inst.date == "2022"
    assert inst.country == "C"
    assert inst.league == "L"
    assert inst.team_home == "HT"
    assert inst.team_away == "AT"
    assert inst.id == "0a15feb03cd4a0afa176"
    assert inst.summary.is_empty()
    assert inst.predictions == {}
    assert not inst.played


def test_match_repr_short():
    inst = lib.models.Match("2022", "C", "L", "HT", "AT")
    assert inst.repr_short() == "2022 - HT - AT"


def test_match_add_prediction():
    inst = lib.models.Match("2022", "C", "L", "HT", "AT")
    pred1 = lib.models.Prediction(lib.models.PredictionEvents.CARD_RED, 90)
    pred2 = lib.models.Prediction(lib.models.PredictionEvents.CARD_RED, 23.3)

    inst.add_prediction(pred1)
    inst.add_prediction(pred2)

    assert inst.predictions[pred1.id].probability == 90
    assert inst.predictions[pred2.id].probability == 23.3


def test_match_update_prediction_not_existing():
    inst = lib.models.Match("2022", "C", "L", "HT", "AT")
    pred1 = lib.models.Prediction(lib.models.PredictionEvents.CARD_RED, 90)

    inst.update_prediction(pred1.id, True)

    assert inst.predictions == {}


def test_match_update_prediction_existing():
    inst = lib.models.Match("2022", "C", "L", "HT", "AT")
    pred1 = lib.models.Prediction(lib.models.PredictionEvents.CARD_RED, 90, expected=False)
    inst.add_prediction(pred1)
    inst.update_prediction(pred1.id, True)

    assert inst.predictions[pred1.id]
