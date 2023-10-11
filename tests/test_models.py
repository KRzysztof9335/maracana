"Tests for models"
import lib.models

def test_participant_class():
    assert "HOME" == lib.models.Participant.HOME.name
    assert "AWAY" == lib.models.Participant.AWAY.name


# =================================================================================================

def test_prediction_creation():
    inst = lib.models.Prediction("aaaa", lib.models.PredictionEvents.CARD_RED, 70.7)

    assert inst.id == "aaaa"
    assert inst.name.value == "card_red"
    assert inst.probability == 70.7
    assert inst.course == 1.1
    assert inst.expected
    assert inst.real == None
    assert inst.guessed == None


def test_prediction_update_guessed():
    inst = lib.models.Prediction("aaaa", lib.models.PredictionEvents.CARD_RED, 70.7, expected=False)
    assert not inst.expected
    assert inst.real == None
    assert inst.guessed == None

    inst.update_prediction(False)

    assert not inst.real
    assert inst.guessed


def test_prediction_update_not_guessed():
    inst = lib.models.Prediction("aaaa", lib.models.PredictionEvents.CARD_RED, 70.7, expected=False)
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
