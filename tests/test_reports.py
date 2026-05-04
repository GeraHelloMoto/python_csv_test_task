import pytest
from app.reports import ClickbaitReport, VideoMetrics

@pytest.fixture
def sample_data():
    return [
        VideoMetrics("High CTR, low retention", 20.0, 30.0),
        VideoMetrics("Low CTR, low retention", 10.0, 25.0),
        VideoMetrics("High CTR, high retention", 25.0, 50.0),
        VideoMetrics("Exactly 15 CTR", 15.0, 39.0),   
        VideoMetrics("Exactly 40 retention", 17.0, 40.0),  
        VideoMetrics("Valid 1", 18.5, 35.0),
        VideoMetrics("Valid 2", 22.1, 20.0),
    ]

def test_clickbait_filter(sample_data):
    report = ClickbaitReport()
    result = report.generate(sample_data)
    titles = [r["title"] for r in result]
    assert "High CTR, low retention" in titles
    assert "Valid 1" in titles
    assert "Valid 2" in titles
    assert "Low CTR, low retention" not in titles
    assert "High CTR, high retention" not in titles
    assert "Exactly 15 CTR" not in titles
    assert "Exactly 40 retention" not in titles

def test_clickbait_sorting(sample_data):
    report = ClickbaitReport()
    result = report.generate(sample_data)
    ctr_values = [r["ctr"] for r in result]
    for i in range(len(ctr_values) - 1):
        assert ctr_values[i] >= ctr_values[i+1]
    assert ctr_values[0] == 22.1
    assert ctr_values[1] == 20.0
    assert ctr_values[2] == 18.5

def test_empty_input():
    report = ClickbaitReport()
    assert report.generate([]) == []