def solution(s: str) -> int:
    def append_compressed(parts: list, sub_str: str, count: int) -> None:
        if count > 1:
            parts.append(str(count))

        parts.append(sub_str)

    optimal_compression_size = len(s)

    for window_size in range(1, (len(s) // 2) + 2):

        start = 0

        compressed_parts = []
        prev_sub = s[0: window_size]
        duplicate_count = 1

        for start in range(window_size, len(s) - window_size + 1, window_size):

            curr_sub = s[start: start + window_size]

            if curr_sub == prev_sub:
                duplicate_count += 1
            else:
                append_compressed(compressed_parts, prev_sub, duplicate_count)

                prev_sub = curr_sub
                duplicate_count = 1

        append_compressed(compressed_parts, prev_sub, duplicate_count)
        compressed_parts.append(s[start + window_size:])
        compressed_length = sum(len(c) for c in compressed_parts)

        optimal_compression_size = min(optimal_compression_size, compressed_length)

    return optimal_compression_size
