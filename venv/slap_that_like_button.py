import enum
class LikeState(enum.Enum):
    empty = enum.auto()
    liked = enum.auto()
    disliked = enum.auto()


slap_like_transitions = {
    LikeState.empty: LikeState.liked,
    LikeState.liked: LikeState.empty,
    LikeState.disliked: LikeState.liked,
}

slap_dislike_transitions = {
    LikeState.empty: LikeState.disliked,
    LikeState.liked: LikeState.disliked,
    LikeState.disliked: LikeState.empty,
}


def slap_like(s: LikeState) -> LikeState:
    return slap_like_transitions[s]


def slap_dislike(s: LikeState) -> LikeState:
    return slap_dislike_transitions[s]


def slap_many(s: LikeState, slaps: str) -> LikeState:
    for c in slaps:
        c = c.lower()
        if c == 'l':
            s = slap_like(s)
        elif c == 'd':
            s = slap_dislike(s)
        else:
            raise ValueError('invalid slap')
    return s

def main():
    # Test cases
    print(slap_many(LikeState.empty, 'll'))  # Should print LikeState.empty
    print(slap_many(LikeState.empty, 'dd'))  # Should print LikeState.empty
    print(slap_many(LikeState.empty, 'ld'))  # Should print LikeState.disliked
    print(slap_many(LikeState.empty, 'dl'))  # Should print LikeState.liked
    print(slap_many(LikeState.empty, 'ldd'))  # Should print LikeState.empty
    print(slap_many(LikeState.empty, 'lldd'))  # Should print LikeState.empty
    print(slap_many(LikeState.empty, 'ddl'))  # Should print LikeState.liked

if __name__ == "__main__":
    main()