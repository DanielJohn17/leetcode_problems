func longestPalindrome(s string) string {
	left, right := 0, 1

	expand := func(l, r int) {
		for l >= 0 && r < len(s) && s[l] == s[r] {
			if right-left < r-l+1 {
				left = l
				right = r + 1
			}
			l--
			r++
		}
	}

	for i, _ := range s {
		expand(i, i)
		expand(i, i+1)
	}

	return s[left:right]
}