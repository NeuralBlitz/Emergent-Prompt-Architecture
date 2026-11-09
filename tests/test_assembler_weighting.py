import pytest

from epa.assembler import GenesisAssembler
from epa.config import SystemMode
from epa.onton import Onton, OntonType


def test_mode_weighting_does_not_mutate_original_onton():
    original = Onton(
        id="ethical-test",
        content="Preserve ethical constraints",
        type=OntonType.ETHICAL,
        weight=0.4,
    )
    assembler = GenesisAssembler(lattice=None, mode=SystemMode.SENTIO)

    weighted = assembler._apply_mode_weighting([original])

    assert weighted[0] is not original
    assert weighted[0].weight == pytest.approx(0.6)
    assert original.weight == pytest.approx(0.4)


def test_repeated_mode_weighting_does_not_compound():
    original = Onton(
        id="ethical-repeat-test",
        content="Preserve ethical constraints",
        type=OntonType.ETHICAL,
        weight=0.4,
    )
    assembler = GenesisAssembler(lattice=None, mode=SystemMode.SENTIO)

    first = assembler._apply_mode_weighting([original])[0]
    second = assembler._apply_mode_weighting([original])[0]

    assert first.weight == pytest.approx(0.6)
    assert second.weight == pytest.approx(0.6)
    assert original.weight == pytest.approx(0.4)
