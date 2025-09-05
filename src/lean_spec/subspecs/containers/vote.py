"""Vote Containers."""

from lean_spec.types import Bytes32, StrictBaseModel, Uint64

from .checkpoint import Checkpoint


class Vote(StrictBaseModel):
    """Represents an attester's vote for chain head."""

    attester: Uint64
    """The index of the voting attester."""

    slot: Uint64
    """The slot for which this vote is cast."""

    head: Checkpoint
    """The attester's perceived head of the chain."""

    target: Checkpoint
    """The justified checkpoint the attester is voting for."""

    source: Checkpoint
    """The last justified checkpoint known to the attester."""


class SignedVote(StrictBaseModel):
    """A container for a vote and its corresponding signature."""

    data: Vote
    """The vote data."""

    signature: Bytes32
    """
    The signature of the vote data.

    Note: Bytes32 is a placeholder; the actual signature is much larger.
    """
