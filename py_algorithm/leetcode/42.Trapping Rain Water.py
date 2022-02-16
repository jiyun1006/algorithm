#!/usr/bin/env python
# coding: utf-8

# In[25]:


# 왼쪽에서 오른쪽으로 가면서 변곡점을 만났을 때, 빗물의 양을 더해간다. 
# 모든 테스트 케이스에 대응하려다 보니, 코드가 길어지고 지저분해졌다.

def trap(height: List[int]) -> int:
        if len(height) > 1:
            i, ans, temp, cnt = 0, 0, 0, 0
            left, max_temp = [], (0,0)

            while i != len(height):
                if height[i] == 0:
                    i += 1
                    cnt += 1
                    continue
                if left:
                    cnt += 1
                    if height[i] >= left[0][0] and cnt >= 2:
                        ans += ((i - left[0][1] - 1) * (left[0][0]) - temp)
                        temp = 0
                        left.pop()
                        left.append((height[i], i))
                        i += 1
                        cnt = 0
                    else:
                        temp += height[i]
                        max_temp = max(max_temp, (height[i], i))
                        i += 1

                else:
                    left.append((height[i], i))
                    i += 1

            if left[0][1] != len(height)-1 :
                if max_temp != (0,0) and max_temp[1] != len(height) -1:
                    for j in range(max_temp[1], len(height)):
                        temp -= height[j]
                    ans += (( max_temp[1] - left[0][1] - 1) * (max_temp[0]) -temp )

            return ans
        else:
            return 0


# In[ ]:


# 투 포인터를 이용한 방법.
# 왼쪽의 max지점과 오른쪽의 max지점을 비교해서 물의 양을 구한다. (한쪽의 max가 더 크면, 최종적으로 어차피 더해질 빗물의 양이다.)

def trap(height: List[int]) -> int:
        if not height:
            return 0
        left, right = 0, len(height)-1
        l_max, r_max = height[left], height[right]
        ans = 0
        while left <= right:
            l_max, r_max = max(l_max, height[left]), max(r_max, height[right])
            if l_max <= r_max:
                ans += l_max - height[left]
                left += 1
            else:
                ans += r_max - height[right]
                right -= 1
                
        return ans

