\ Model BBER_BBU
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  y_bar[BBU_111_B_0_1_21_dep_right,BBU_13_A_0_1_21_arr_right]
   + y_bar[BBU_13_A_0_1_21_arr_right,BBU_13_A_0_1_21_dep_left]
   + y_bar[BBU_13_A_0_1_21_dep_left,BBU_112_B_0_1_21_arr_right]
   + y_bar[BBU_112_B_0_1_21_arr_right,BBU_112_B_0_1_21_dep_right]
   + 2 y_bar[BBU_112_B_0_1_21_dep_right,henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12]
   + 2 y_bar[BBU_112_B_0_1_21_dep_right,henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12]
   + 2 y_bar[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12,BBU_111_B_0_1_21_arr_right]
   + 2 y_bar[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12,BBU_111_B_0_1_21_arr_right]
   + y_bar[BBU_111_B_0_1_21_arr_right,BBU_111_B_0_1_21_dep_right]
   + y_bar[BBU_111_B_200_2_21_dep_right,BBU_13_A_200_2_21_arr_right]
   + y_bar[BBU_13_A_200_2_21_arr_right,BBU_13_A_200_2_21_dep_left]
   + y_bar[BBU_13_A_200_2_21_dep_left,BBU_112_B_200_2_21_arr_right]
   + y_bar[BBU_112_B_200_2_21_arr_right,BBU_112_B_200_2_21_dep_right]
   + 2 y_bar[BBU_112_B_200_2_21_dep_right,henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12]
   + 2 y_bar[BBU_112_B_200_2_21_dep_right,henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12]
   + 2 y_bar[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12,BBU_111_B_200_2_21_arr_right]
   + 2 y_bar[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12,BBU_111_B_200_2_21_arr_right]
   + y_bar[BBU_111_B_200_2_21_arr_right,BBU_111_B_200_2_21_dep_right]
   - 76.24304059982452 h[BBU_111_B_0_1_21_dep_right,BBU_13_A_0_1_21_arr_right]
   - 71.24304059982452 h[BBU_13_A_0_1_21_arr_right,BBU_13_A_0_1_21_dep_left]
   - 76.24304059982452 h[BBU_13_A_0_1_21_dep_left,BBU_112_B_0_1_21_arr_right]
   - 86.24304059982452 h[BBU_112_B_0_1_21_arr_right,BBU_112_B_0_1_21_dep_right]
   - 1039.701284198771 h[BBU_112_B_0_1_21_dep_right,henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12]
   + 320 h[BBU_112_B_0_1_21_dep_right,henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12]
   - 32.24304059982452 h[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12,BBU_111_B_0_1_21_arr_right]
   + 258 h[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12,BBU_111_B_0_1_21_arr_right]
   - 86.24304059982452 h[BBU_111_B_0_1_21_arr_right,BBU_111_B_0_1_21_dep_right]
   - 76.24304059982452 h[BBU_111_B_200_2_21_dep_right,BBU_13_A_200_2_21_arr_right]
   - 71.24304059982452 h[BBU_13_A_200_2_21_arr_right,BBU_13_A_200_2_21_dep_left]
   - 76.24304059982452 h[BBU_13_A_200_2_21_dep_left,BBU_112_B_200_2_21_arr_right]
   - 86.24304059982452 h[BBU_112_B_200_2_21_arr_right,BBU_112_B_200_2_21_dep_right]
   - 98.89114886602326 h[BBU_112_B_200_2_21_dep_right,henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12]
   + 320 h[BBU_112_B_200_2_21_dep_right,henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12]
   - 1101.701284198771 h[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12,BBU_111_B_200_2_21_arr_right]
   + 258 h[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12,BBU_111_B_200_2_21_arr_right]
   - 86.24304059982452 h[BBU_111_B_200_2_21_arr_right,BBU_111_B_200_2_21_dep_right]
   + 460.2152029991227 b[1] + 1710.159527797719 b[2]
   + 460.2152029991227 b[3] + 1838.807636063917 b[4]
Subject To
 slack_BBU_111_B_0_1_21_dep_rightBBU_13_A_0_1_21_arr_right:
   - 200 p[BBU_111_B_0_1_21_dep_right,BBU_13_A_0_1_21_arr_right]
   + pi[BBU_111_B_0_1_21_dep_right] - pi[BBU_13_A_0_1_21_arr_right]
   + y[BBU_111_B_0_1_21_dep_right,BBU_13_A_0_1_21_arr_right]
   + 15 h[BBU_111_B_0_1_21_dep_right,BBU_13_A_0_1_21_arr_right] = 0
 slack_BBU_13_A_0_1_21_arr_rightBBU_13_A_0_1_21_dep_left:
   - 200 p[BBU_13_A_0_1_21_arr_right,BBU_13_A_0_1_21_dep_left]
   + pi[BBU_13_A_0_1_21_arr_right] - pi[BBU_13_A_0_1_21_dep_left]
   + y[BBU_13_A_0_1_21_arr_right,BBU_13_A_0_1_21_dep_left]
   + 20 h[BBU_13_A_0_1_21_arr_right,BBU_13_A_0_1_21_dep_left] = 0
 slack_BBU_13_A_0_1_21_dep_leftBBU_112_B_0_1_21_arr_right:
   - 200 p[BBU_13_A_0_1_21_dep_left,BBU_112_B_0_1_21_arr_right]
   + pi[BBU_13_A_0_1_21_dep_left] - pi[BBU_112_B_0_1_21_arr_right]
   + y[BBU_13_A_0_1_21_dep_left,BBU_112_B_0_1_21_arr_right]
   + 15 h[BBU_13_A_0_1_21_dep_left,BBU_112_B_0_1_21_arr_right] = 0
 slack_BBU_112_B_0_1_21_arr_rightBBU_112_B_0_1_21_dep_right:
   - 200 p[BBU_112_B_0_1_21_arr_right,BBU_112_B_0_1_21_dep_right]
   + pi[BBU_112_B_0_1_21_arr_right] - pi[BBU_112_B_0_1_21_dep_right]
   + y[BBU_112_B_0_1_21_arr_right,BBU_112_B_0_1_21_dep_right]
   + 5 h[BBU_112_B_0_1_21_arr_right,BBU_112_B_0_1_21_dep_right] = 0
 slack_BBU_112_B_0_1_21_dep_righthenkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12:
   - 200 p[BBU_112_B_0_1_21_dep_right,henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12]
   + pi[BBU_112_B_0_1_21_dep_right]
   - pi[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12]
   + y[BBU_112_B_0_1_21_dep_right,henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12]
   + 61 h[BBU_112_B_0_1_21_dep_right,henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12]
   = 0
 slack_BBU_112_B_0_1_21_dep_righthenkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12:
   - 200 p[BBU_112_B_0_1_21_dep_right,henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12]
   + pi[BBU_112_B_0_1_21_dep_right]
   - pi[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12]
   + y[BBU_112_B_0_1_21_dep_right,henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12]
   + 161 h[BBU_112_B_0_1_21_dep_right,henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12]
   = 0
 slack_henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12BBU_111_B_0_1_21_arr_right:
   - 200 p[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12,BBU_111_B_0_1_21_arr_right]
   + pi[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12]
   - pi[BBU_111_B_0_1_21_arr_right]
   + y[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12,BBU_111_B_0_1_21_arr_right]
   + 30 h[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12,BBU_111_B_0_1_21_arr_right]
   = 0
 slack_henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12BBU_111_B_0_1_21_arr_right:
   - 200 p[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12,BBU_111_B_0_1_21_arr_right]
   + pi[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12]
   - pi[BBU_111_B_0_1_21_arr_right]
   + y[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12,BBU_111_B_0_1_21_arr_right]
   + 130 h[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12,BBU_111_B_0_1_21_arr_right]
   = 0
 slack_BBU_111_B_0_1_21_arr_rightBBU_111_B_0_1_21_dep_right:
   - 200 p[BBU_111_B_0_1_21_arr_right,BBU_111_B_0_1_21_dep_right]
   - pi[BBU_111_B_0_1_21_dep_right] + pi[BBU_111_B_0_1_21_arr_right]
   + y[BBU_111_B_0_1_21_arr_right,BBU_111_B_0_1_21_dep_right]
   + 5 h[BBU_111_B_0_1_21_arr_right,BBU_111_B_0_1_21_dep_right] = 0
 slack_BBU_111_B_200_2_21_dep_rightBBU_13_A_200_2_21_arr_right:
   - 200 p[BBU_111_B_200_2_21_dep_right,BBU_13_A_200_2_21_arr_right]
   + pi[BBU_111_B_200_2_21_dep_right] - pi[BBU_13_A_200_2_21_arr_right]
   + y[BBU_111_B_200_2_21_dep_right,BBU_13_A_200_2_21_arr_right]
   + 15 h[BBU_111_B_200_2_21_dep_right,BBU_13_A_200_2_21_arr_right] = 0
 slack_BBU_13_A_200_2_21_arr_rightBBU_13_A_200_2_21_dep_left:
   - 200 p[BBU_13_A_200_2_21_arr_right,BBU_13_A_200_2_21_dep_left]
   + pi[BBU_13_A_200_2_21_arr_right] - pi[BBU_13_A_200_2_21_dep_left]
   + y[BBU_13_A_200_2_21_arr_right,BBU_13_A_200_2_21_dep_left]
   + 20 h[BBU_13_A_200_2_21_arr_right,BBU_13_A_200_2_21_dep_left] = 0
 slack_BBU_13_A_200_2_21_dep_leftBBU_112_B_200_2_21_arr_right:
   - 200 p[BBU_13_A_200_2_21_dep_left,BBU_112_B_200_2_21_arr_right]
   + pi[BBU_13_A_200_2_21_dep_left] - pi[BBU_112_B_200_2_21_arr_right]
   + y[BBU_13_A_200_2_21_dep_left,BBU_112_B_200_2_21_arr_right]
   + 15 h[BBU_13_A_200_2_21_dep_left,BBU_112_B_200_2_21_arr_right] = 0
 slack_BBU_112_B_200_2_21_arr_rightBBU_112_B_200_2_21_dep_right:
   - 200 p[BBU_112_B_200_2_21_arr_right,BBU_112_B_200_2_21_dep_right]
   + pi[BBU_112_B_200_2_21_arr_right] - pi[BBU_112_B_200_2_21_dep_right]
   + y[BBU_112_B_200_2_21_arr_right,BBU_112_B_200_2_21_dep_right]
   + 5 h[BBU_112_B_200_2_21_arr_right,BBU_112_B_200_2_21_dep_right] = 0
 slack_BBU_112_B_200_2_21_dep_righthenkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12:
   - 200 p[BBU_112_B_200_2_21_dep_right,henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12]
   + pi[BBU_112_B_200_2_21_dep_right]
   - pi[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12]
   + y[BBU_112_B_200_2_21_dep_right,henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12]
   + 61 h[BBU_112_B_200_2_21_dep_right,henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12]
   = 0
 slack_BBU_112_B_200_2_21_dep_righthenkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12:
   - 200 p[BBU_112_B_200_2_21_dep_right,henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12]
   + pi[BBU_112_B_200_2_21_dep_right]
   - pi[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12]
   + y[BBU_112_B_200_2_21_dep_right,henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12]
   + 161 h[BBU_112_B_200_2_21_dep_right,henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12]
   = 0
 slack_henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12BBU_111_B_200_2_21_arr_right:
   - 200 p[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12,BBU_111_B_200_2_21_arr_right]
   + pi[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12]
   - pi[BBU_111_B_200_2_21_arr_right]
   + y[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12,BBU_111_B_200_2_21_arr_right]
   + 30 h[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12,BBU_111_B_200_2_21_arr_right]
   = 0
 slack_henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12BBU_111_B_200_2_21_arr_right:
   - 200 p[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12,BBU_111_B_200_2_21_arr_right]
   + pi[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12]
   - pi[BBU_111_B_200_2_21_arr_right]
   + y[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12,BBU_111_B_200_2_21_arr_right]
   + 130 h[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12,BBU_111_B_200_2_21_arr_right]
   = 0
 slack_BBU_111_B_200_2_21_arr_rightBBU_111_B_200_2_21_dep_right:
   - 200 p[BBU_111_B_200_2_21_arr_right,BBU_111_B_200_2_21_dep_right]
   - pi[BBU_111_B_200_2_21_dep_right] + pi[BBU_111_B_200_2_21_arr_right]
   + y[BBU_111_B_200_2_21_arr_right,BBU_111_B_200_2_21_dep_right]
   + 5 h[BBU_111_B_200_2_21_arr_right,BBU_111_B_200_2_21_dep_right] = 0
 artificial_upper_bound_BBU_111_B_0_1_21_dep_rightBBU_13_A_0_1_21_arr_right:
   y[BBU_111_B_0_1_21_dep_right,BBU_13_A_0_1_21_arr_right]
   + 199 h[BBU_111_B_0_1_21_dep_right,BBU_13_A_0_1_21_arr_right] <= 199
 upper_bound_coupled_BBU_111_B_0_1_21_dep_rightBBU_13_A_0_1_21_arr_right:
   y_bar[BBU_111_B_0_1_21_dep_right,BBU_13_A_0_1_21_arr_right] <= 0
 lower_bound_coupled_BBU_111_B_0_1_21_dep_rightBBU_13_A_0_1_21_arr_right:
   - y[BBU_111_B_0_1_21_dep_right,BBU_13_A_0_1_21_arr_right]
   + y_bar[BBU_111_B_0_1_21_dep_right,BBU_13_A_0_1_21_arr_right]
   - 199 h[BBU_111_B_0_1_21_dep_right,BBU_13_A_0_1_21_arr_right] >= -199
 artificial_upper_bound_BBU_13_A_0_1_21_arr_rightBBU_13_A_0_1_21_dep_left:
   y[BBU_13_A_0_1_21_arr_right,BBU_13_A_0_1_21_dep_left]
   + 39 h[BBU_13_A_0_1_21_arr_right,BBU_13_A_0_1_21_dep_left] <= 199
 upper_bound_coupled_BBU_13_A_0_1_21_arr_rightBBU_13_A_0_1_21_dep_left:
   y_bar[BBU_13_A_0_1_21_arr_right,BBU_13_A_0_1_21_dep_left]
   - 160 h[BBU_13_A_0_1_21_arr_right,BBU_13_A_0_1_21_dep_left] <= 0
 lower_bound_coupled_BBU_13_A_0_1_21_arr_rightBBU_13_A_0_1_21_dep_left:
   - y[BBU_13_A_0_1_21_arr_right,BBU_13_A_0_1_21_dep_left]
   + y_bar[BBU_13_A_0_1_21_arr_right,BBU_13_A_0_1_21_dep_left]
   - 199 h[BBU_13_A_0_1_21_arr_right,BBU_13_A_0_1_21_dep_left] >= -199
 artificial_upper_bound_BBU_13_A_0_1_21_dep_leftBBU_112_B_0_1_21_arr_right:
   y[BBU_13_A_0_1_21_dep_left,BBU_112_B_0_1_21_arr_right]
   + 199 h[BBU_13_A_0_1_21_dep_left,BBU_112_B_0_1_21_arr_right] <= 199
 upper_bound_coupled_BBU_13_A_0_1_21_dep_leftBBU_112_B_0_1_21_arr_right:
   y_bar[BBU_13_A_0_1_21_dep_left,BBU_112_B_0_1_21_arr_right] <= 0
 lower_bound_coupled_BBU_13_A_0_1_21_dep_leftBBU_112_B_0_1_21_arr_right:
   - y[BBU_13_A_0_1_21_dep_left,BBU_112_B_0_1_21_arr_right]
   + y_bar[BBU_13_A_0_1_21_dep_left,BBU_112_B_0_1_21_arr_right]
   - 199 h[BBU_13_A_0_1_21_dep_left,BBU_112_B_0_1_21_arr_right] >= -199
 artificial_upper_bound_BBU_112_B_0_1_21_arr_rightBBU_112_B_0_1_21_dep_right:
   y[BBU_112_B_0_1_21_arr_right,BBU_112_B_0_1_21_dep_right]
   + 104 h[BBU_112_B_0_1_21_arr_right,BBU_112_B_0_1_21_dep_right] <= 199
 upper_bound_coupled_BBU_112_B_0_1_21_arr_rightBBU_112_B_0_1_21_dep_right:
   y_bar[BBU_112_B_0_1_21_arr_right,BBU_112_B_0_1_21_dep_right]
   - 95 h[BBU_112_B_0_1_21_arr_right,BBU_112_B_0_1_21_dep_right] <= 0
 lower_bound_coupled_BBU_112_B_0_1_21_arr_rightBBU_112_B_0_1_21_dep_right:
   - y[BBU_112_B_0_1_21_arr_right,BBU_112_B_0_1_21_dep_right]
   + y_bar[BBU_112_B_0_1_21_arr_right,BBU_112_B_0_1_21_dep_right]
   - 199 h[BBU_112_B_0_1_21_arr_right,BBU_112_B_0_1_21_dep_right] >= -199
 artificial_upper_bound_BBU_112_B_0_1_21_dep_righthenkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12:
   y[BBU_112_B_0_1_21_dep_right,henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12]
   + 199 h[BBU_112_B_0_1_21_dep_right,henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12]
   <= 199
 upper_bound_coupled_BBU_112_B_0_1_21_dep_righthenkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12:
   y_bar[BBU_112_B_0_1_21_dep_right,henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12]
   <= 0
 lower_bound_coupled_BBU_112_B_0_1_21_dep_righthenkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12:
   - y[BBU_112_B_0_1_21_dep_right,henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12]
   + y_bar[BBU_112_B_0_1_21_dep_right,henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12]
   - 199 h[BBU_112_B_0_1_21_dep_right,henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12]
   >= -199
 artificial_upper_bound_BBU_112_B_0_1_21_dep_righthenkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12:
   y[BBU_112_B_0_1_21_dep_right,henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12]
   + 199 h[BBU_112_B_0_1_21_dep_right,henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12]
   <= 199
 upper_bound_coupled_BBU_112_B_0_1_21_dep_righthenkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12:
   y_bar[BBU_112_B_0_1_21_dep_right,henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12]
   <= 0
 lower_bound_coupled_BBU_112_B_0_1_21_dep_righthenkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12:
   - y[BBU_112_B_0_1_21_dep_right,henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12]
   + y_bar[BBU_112_B_0_1_21_dep_right,henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12]
   - 199 h[BBU_112_B_0_1_21_dep_right,henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12]
   >= -199
 artificial_upper_bound_henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12BBU_111_B_0_1_21_arr_right:
   y[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12,BBU_111_B_0_1_21_arr_right]
   + 199 h[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12,BBU_111_B_0_1_21_arr_right]
   <= 199
 upper_bound_coupled_henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12BBU_111_B_0_1_21_arr_right:
   y_bar[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12,BBU_111_B_0_1_21_arr_right]
   <= 0
 lower_bound_coupled_henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12BBU_111_B_0_1_21_arr_right:
   - y[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12,BBU_111_B_0_1_21_arr_right]
   + y_bar[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12,BBU_111_B_0_1_21_arr_right]
   - 199 h[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12,BBU_111_B_0_1_21_arr_right]
   >= -199
 artificial_upper_bound_henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12BBU_111_B_0_1_21_arr_right:
   y[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12,BBU_111_B_0_1_21_arr_right]
   + 199 h[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12,BBU_111_B_0_1_21_arr_right]
   <= 199
 upper_bound_coupled_henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12BBU_111_B_0_1_21_arr_right:
   y_bar[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12,BBU_111_B_0_1_21_arr_right]
   <= 0
 lower_bound_coupled_henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12BBU_111_B_0_1_21_arr_right:
   - y[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12,BBU_111_B_0_1_21_arr_right]
   + y_bar[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12,BBU_111_B_0_1_21_arr_right]
   - 199 h[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12,BBU_111_B_0_1_21_arr_right]
   >= -199
 artificial_upper_bound_BBU_111_B_0_1_21_arr_rightBBU_111_B_0_1_21_dep_right:
   y[BBU_111_B_0_1_21_arr_right,BBU_111_B_0_1_21_dep_right]
   + 104 h[BBU_111_B_0_1_21_arr_right,BBU_111_B_0_1_21_dep_right] <= 199
 upper_bound_coupled_BBU_111_B_0_1_21_arr_rightBBU_111_B_0_1_21_dep_right:
   y_bar[BBU_111_B_0_1_21_arr_right,BBU_111_B_0_1_21_dep_right]
   - 95 h[BBU_111_B_0_1_21_arr_right,BBU_111_B_0_1_21_dep_right] <= 0
 lower_bound_coupled_BBU_111_B_0_1_21_arr_rightBBU_111_B_0_1_21_dep_right:
   - y[BBU_111_B_0_1_21_arr_right,BBU_111_B_0_1_21_dep_right]
   + y_bar[BBU_111_B_0_1_21_arr_right,BBU_111_B_0_1_21_dep_right]
   - 199 h[BBU_111_B_0_1_21_arr_right,BBU_111_B_0_1_21_dep_right] >= -199
 artificial_upper_bound_BBU_111_B_200_2_21_dep_rightBBU_13_A_200_2_21_arr_right:
   y[BBU_111_B_200_2_21_dep_right,BBU_13_A_200_2_21_arr_right]
   + 199 h[BBU_111_B_200_2_21_dep_right,BBU_13_A_200_2_21_arr_right]
   <= 199
 upper_bound_coupled_BBU_111_B_200_2_21_dep_rightBBU_13_A_200_2_21_arr_right:
   y_bar[BBU_111_B_200_2_21_dep_right,BBU_13_A_200_2_21_arr_right] <= 0
 lower_bound_coupled_BBU_111_B_200_2_21_dep_rightBBU_13_A_200_2_21_arr_right:
   - y[BBU_111_B_200_2_21_dep_right,BBU_13_A_200_2_21_arr_right]
   + y_bar[BBU_111_B_200_2_21_dep_right,BBU_13_A_200_2_21_arr_right]
   - 199 h[BBU_111_B_200_2_21_dep_right,BBU_13_A_200_2_21_arr_right]
   >= -199
 artificial_upper_bound_BBU_13_A_200_2_21_arr_rightBBU_13_A_200_2_21_dep_left:
   y[BBU_13_A_200_2_21_arr_right,BBU_13_A_200_2_21_dep_left]
   + 39 h[BBU_13_A_200_2_21_arr_right,BBU_13_A_200_2_21_dep_left] <= 199
 upper_bound_coupled_BBU_13_A_200_2_21_arr_rightBBU_13_A_200_2_21_dep_left:
   y_bar[BBU_13_A_200_2_21_arr_right,BBU_13_A_200_2_21_dep_left]
   - 160 h[BBU_13_A_200_2_21_arr_right,BBU_13_A_200_2_21_dep_left] <= 0
 lower_bound_coupled_BBU_13_A_200_2_21_arr_rightBBU_13_A_200_2_21_dep_left:
   - y[BBU_13_A_200_2_21_arr_right,BBU_13_A_200_2_21_dep_left]
   + y_bar[BBU_13_A_200_2_21_arr_right,BBU_13_A_200_2_21_dep_left]
   - 199 h[BBU_13_A_200_2_21_arr_right,BBU_13_A_200_2_21_dep_left] >= -199
 artificial_upper_bound_BBU_13_A_200_2_21_dep_leftBBU_112_B_200_2_21_arr_right:
   y[BBU_13_A_200_2_21_dep_left,BBU_112_B_200_2_21_arr_right]
   + 199 h[BBU_13_A_200_2_21_dep_left,BBU_112_B_200_2_21_arr_right] <= 199
 upper_bound_coupled_BBU_13_A_200_2_21_dep_leftBBU_112_B_200_2_21_arr_right:
   y_bar[BBU_13_A_200_2_21_dep_left,BBU_112_B_200_2_21_arr_right] <= 0
 lower_bound_coupled_BBU_13_A_200_2_21_dep_leftBBU_112_B_200_2_21_arr_right:
   - y[BBU_13_A_200_2_21_dep_left,BBU_112_B_200_2_21_arr_right]
   + y_bar[BBU_13_A_200_2_21_dep_left,BBU_112_B_200_2_21_arr_right]
   - 199 h[BBU_13_A_200_2_21_dep_left,BBU_112_B_200_2_21_arr_right]
   >= -199
 artificial_upper_bound_BBU_112_B_200_2_21_arr_rightBBU_112_B_200_2_21_dep_right:
   y[BBU_112_B_200_2_21_arr_right,BBU_112_B_200_2_21_dep_right]
   + 104 h[BBU_112_B_200_2_21_arr_right,BBU_112_B_200_2_21_dep_right]
   <= 199
 upper_bound_coupled_BBU_112_B_200_2_21_arr_rightBBU_112_B_200_2_21_dep_right:
   y_bar[BBU_112_B_200_2_21_arr_right,BBU_112_B_200_2_21_dep_right]
   - 95 h[BBU_112_B_200_2_21_arr_right,BBU_112_B_200_2_21_dep_right] <= 0
 lower_bound_coupled_BBU_112_B_200_2_21_arr_rightBBU_112_B_200_2_21_dep_right:
   - y[BBU_112_B_200_2_21_arr_right,BBU_112_B_200_2_21_dep_right]
   + y_bar[BBU_112_B_200_2_21_arr_right,BBU_112_B_200_2_21_dep_right]
   - 199 h[BBU_112_B_200_2_21_arr_right,BBU_112_B_200_2_21_dep_right]
   >= -199
 artificial_upper_bound_BBU_112_B_200_2_21_dep_righthenkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12:
   y[BBU_112_B_200_2_21_dep_right,henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12]
   + 199 h[BBU_112_B_200_2_21_dep_right,henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12]
   <= 199
 upper_bound_coupled_BBU_112_B_200_2_21_dep_righthenkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12:
   y_bar[BBU_112_B_200_2_21_dep_right,henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12]
   <= 0
 lower_bound_coupled_BBU_112_B_200_2_21_dep_righthenkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12:
   - y[BBU_112_B_200_2_21_dep_right,henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12]
   + y_bar[BBU_112_B_200_2_21_dep_right,henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12]
   - 199 h[BBU_112_B_200_2_21_dep_right,henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12]
   >= -199
 artificial_upper_bound_BBU_112_B_200_2_21_dep_righthenkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12:
   y[BBU_112_B_200_2_21_dep_right,henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12]
   + 199 h[BBU_112_B_200_2_21_dep_right,henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12]
   <= 199
 upper_bound_coupled_BBU_112_B_200_2_21_dep_righthenkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12:
   y_bar[BBU_112_B_200_2_21_dep_right,henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12]
   <= 0
 lower_bound_coupled_BBU_112_B_200_2_21_dep_righthenkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12:
   - y[BBU_112_B_200_2_21_dep_right,henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12]
   + y_bar[BBU_112_B_200_2_21_dep_right,henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12]
   - 199 h[BBU_112_B_200_2_21_dep_right,henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12]
   >= -199
 artificial_upper_bound_henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12BBU_111_B_200_2_21_arr_right:
   y[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12,BBU_111_B_200_2_21_arr_right]
   + 199 h[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12,BBU_111_B_200_2_21_arr_right]
   <= 199
 upper_bound_coupled_henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12BBU_111_B_200_2_21_arr_right:
   y_bar[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12,BBU_111_B_200_2_21_arr_right]
   <= 0
 lower_bound_coupled_henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12BBU_111_B_200_2_21_arr_right:
   - y[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12,BBU_111_B_200_2_21_arr_right]
   + y_bar[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12,BBU_111_B_200_2_21_arr_right]
   - 199 h[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12,BBU_111_B_200_2_21_arr_right]
   >= -199
 artificial_upper_bound_henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12BBU_111_B_200_2_21_arr_right:
   y[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12,BBU_111_B_200_2_21_arr_right]
   + 199 h[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12,BBU_111_B_200_2_21_arr_right]
   <= 199
 upper_bound_coupled_henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12BBU_111_B_200_2_21_arr_right:
   y_bar[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12,BBU_111_B_200_2_21_arr_right]
   <= 0
 lower_bound_coupled_henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12BBU_111_B_200_2_21_arr_right:
   - y[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12,BBU_111_B_200_2_21_arr_right]
   + y_bar[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12,BBU_111_B_200_2_21_arr_right]
   - 199 h[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12,BBU_111_B_200_2_21_arr_right]
   >= -199
 artificial_upper_bound_BBU_111_B_200_2_21_arr_rightBBU_111_B_200_2_21_dep_right:
   y[BBU_111_B_200_2_21_arr_right,BBU_111_B_200_2_21_dep_right]
   + 104 h[BBU_111_B_200_2_21_arr_right,BBU_111_B_200_2_21_dep_right]
   <= 199
 upper_bound_coupled_BBU_111_B_200_2_21_arr_rightBBU_111_B_200_2_21_dep_right:
   y_bar[BBU_111_B_200_2_21_arr_right,BBU_111_B_200_2_21_dep_right]
   - 95 h[BBU_111_B_200_2_21_arr_right,BBU_111_B_200_2_21_dep_right] <= 0
 lower_bound_coupled_BBU_111_B_200_2_21_arr_rightBBU_111_B_200_2_21_dep_right:
   - y[BBU_111_B_200_2_21_arr_right,BBU_111_B_200_2_21_dep_right]
   + y_bar[BBU_111_B_200_2_21_arr_right,BBU_111_B_200_2_21_dep_right]
   - 199 h[BBU_111_B_200_2_21_arr_right,BBU_111_B_200_2_21_dep_right]
   >= -199
 headway_lower_bound_BBU_13_A_0_1_21_arr_rightBBU_13_A_200_2_21_arr_right_BBU_13_A_0_1_21_arr_rightBBU_13_A_0_1_21_dep_leftBBU_13_A_200_2_21_arr_rightBBU_13_A_200_2_21_dep_left:
   - 200 p[BBU_13_A_0_1_21_arr_right,BBU_13_A_200_2_21_arr_right]
   + pi[BBU_13_A_0_1_21_arr_right] - pi[BBU_13_A_200_2_21_arr_right]
   + 25 h[BBU_13_A_0_1_21_arr_right,BBU_13_A_0_1_21_dep_left]
   + 25 h[BBU_13_A_200_2_21_arr_right,BBU_13_A_200_2_21_dep_left] <= 25
 headway_upper_bound_BBU_13_A_0_1_21_arr_rightBBU_13_A_200_2_21_arr_right_BBU_13_A_0_1_21_arr_rightBBU_13_A_0_1_21_dep_leftBBU_13_A_200_2_21_arr_rightBBU_13_A_200_2_21_dep_left:
   200 p[BBU_13_A_0_1_21_arr_right,BBU_13_A_200_2_21_arr_right]
   - pi[BBU_13_A_0_1_21_arr_right] + pi[BBU_13_A_200_2_21_arr_right]
   + 175 h[BBU_13_A_0_1_21_arr_right,BBU_13_A_0_1_21_dep_left]
   + 175 h[BBU_13_A_200_2_21_arr_right,BBU_13_A_200_2_21_dep_left] <= 525
 modulo_i_BBU_13_A_0_1_21_arr_rightBBU_13_A_200_2_21_arr_right_BBU_13_A_0_1_21_arr_right_BBU_13_A_0_1_21_dep_left_BBU_13_A_200_2_21_arr_right_BBU_13_A_200_2_21_dep_left:
   p[BBU_13_A_0_1_21_arr_right,BBU_13_A_200_2_21_arr_right] <= 1
 headway_lower_bound_BBU_13_A_200_2_21_arr_rightBBU_13_A_0_1_21_arr_right_BBU_13_A_0_1_21_arr_rightBBU_13_A_0_1_21_dep_leftBBU_13_A_200_2_21_arr_rightBBU_13_A_200_2_21_dep_left:
   - 200 p[BBU_13_A_200_2_21_arr_right,BBU_13_A_0_1_21_arr_right]
   - pi[BBU_13_A_0_1_21_arr_right] + pi[BBU_13_A_200_2_21_arr_right]
   + 25 h[BBU_13_A_0_1_21_arr_right,BBU_13_A_0_1_21_dep_left]
   + 25 h[BBU_13_A_200_2_21_arr_right,BBU_13_A_200_2_21_dep_left] <= 25
 headway_upper_bound_BBU_13_A_200_2_21_arr_rightBBU_13_A_0_1_21_arr_right_BBU_13_A_0_1_21_arr_rightBBU_13_A_0_1_21_dep_leftBBU_13_A_200_2_21_arr_rightBBU_13_A_200_2_21_dep_left:
   200 p[BBU_13_A_200_2_21_arr_right,BBU_13_A_0_1_21_arr_right]
   + pi[BBU_13_A_0_1_21_arr_right] - pi[BBU_13_A_200_2_21_arr_right]
   + 175 h[BBU_13_A_0_1_21_arr_right,BBU_13_A_0_1_21_dep_left]
   + 175 h[BBU_13_A_200_2_21_arr_right,BBU_13_A_200_2_21_dep_left] <= 525
 modulo_i_BBU_13_A_200_2_21_arr_rightBBU_13_A_0_1_21_arr_right_BBU_13_A_0_1_21_arr_right_BBU_13_A_0_1_21_dep_left_BBU_13_A_200_2_21_arr_right_BBU_13_A_200_2_21_dep_left:
   p[BBU_13_A_200_2_21_arr_right,BBU_13_A_0_1_21_arr_right] <= 1
 headway_lower_bound_BBU_13_A_0_1_21_dep_leftBBU_13_A_200_2_21_arr_right_BBU_13_A_0_1_21_arr_rightBBU_13_A_0_1_21_dep_leftBBU_13_A_200_2_21_arr_rightBBU_13_A_200_2_21_dep_left:
   - 200 p[BBU_13_A_0_1_21_dep_left,BBU_13_A_200_2_21_arr_right]
   + pi[BBU_13_A_0_1_21_dep_left] - pi[BBU_13_A_200_2_21_arr_right]
   + 17 h[BBU_13_A_0_1_21_arr_right,BBU_13_A_0_1_21_dep_left]
   + 17 h[BBU_13_A_200_2_21_arr_right,BBU_13_A_200_2_21_dep_left] <= 17
 headway_upper_bound_BBU_13_A_0_1_21_dep_leftBBU_13_A_200_2_21_arr_right_BBU_13_A_0_1_21_arr_rightBBU_13_A_0_1_21_dep_leftBBU_13_A_200_2_21_arr_rightBBU_13_A_200_2_21_dep_left:
   200 p[BBU_13_A_0_1_21_dep_left,BBU_13_A_200_2_21_arr_right]
   - pi[BBU_13_A_0_1_21_dep_left] + pi[BBU_13_A_200_2_21_arr_right]
   + 183 h[BBU_13_A_0_1_21_arr_right,BBU_13_A_0_1_21_dep_left]
   + 183 h[BBU_13_A_200_2_21_arr_right,BBU_13_A_200_2_21_dep_left] <= 549
 modulo_i_BBU_13_A_0_1_21_dep_leftBBU_13_A_200_2_21_arr_right_BBU_13_A_0_1_21_arr_right_BBU_13_A_0_1_21_dep_left_BBU_13_A_200_2_21_arr_right_BBU_13_A_200_2_21_dep_left:
   p[BBU_13_A_0_1_21_dep_left,BBU_13_A_200_2_21_arr_right] <= 1
 headway_lower_bound_BBU_13_A_200_2_21_dep_leftBBU_13_A_0_1_21_arr_right_BBU_13_A_0_1_21_arr_rightBBU_13_A_0_1_21_dep_leftBBU_13_A_200_2_21_arr_rightBBU_13_A_200_2_21_dep_left:
   - 200 p[BBU_13_A_200_2_21_dep_left,BBU_13_A_0_1_21_arr_right]
   - pi[BBU_13_A_0_1_21_arr_right] + pi[BBU_13_A_200_2_21_dep_left]
   + 17 h[BBU_13_A_0_1_21_arr_right,BBU_13_A_0_1_21_dep_left]
   + 17 h[BBU_13_A_200_2_21_arr_right,BBU_13_A_200_2_21_dep_left] <= 17
 headway_upper_bound_BBU_13_A_200_2_21_dep_leftBBU_13_A_0_1_21_arr_right_BBU_13_A_0_1_21_arr_rightBBU_13_A_0_1_21_dep_leftBBU_13_A_200_2_21_arr_rightBBU_13_A_200_2_21_dep_left:
   200 p[BBU_13_A_200_2_21_dep_left,BBU_13_A_0_1_21_arr_right]
   + pi[BBU_13_A_0_1_21_arr_right] - pi[BBU_13_A_200_2_21_dep_left]
   + 183 h[BBU_13_A_0_1_21_arr_right,BBU_13_A_0_1_21_dep_left]
   + 183 h[BBU_13_A_200_2_21_arr_right,BBU_13_A_200_2_21_dep_left] <= 549
 modulo_i_BBU_13_A_200_2_21_dep_leftBBU_13_A_0_1_21_arr_right_BBU_13_A_0_1_21_arr_right_BBU_13_A_0_1_21_dep_left_BBU_13_A_200_2_21_arr_right_BBU_13_A_200_2_21_dep_left:
   p[BBU_13_A_200_2_21_dep_left,BBU_13_A_0_1_21_arr_right] <= 1
 conflict_free_lower_1_BBU_13_A_0_1_21_arr_rightBBU_13_A_0_1_21_dep_leftBBU_13_A_200_2_21_arr_rightBBU_13_A_200_2_21_dep_left:
   - p[BBU_13_A_0_1_21_arr_right,BBU_13_A_0_1_21_dep_left]
   + p[BBU_13_A_0_1_21_arr_right,BBU_13_A_200_2_21_arr_right]
   - p[BBU_13_A_0_1_21_dep_left,BBU_13_A_200_2_21_arr_right]
   + h[BBU_13_A_0_1_21_arr_right,BBU_13_A_0_1_21_dep_left]
   + h[BBU_13_A_200_2_21_arr_right,BBU_13_A_200_2_21_dep_left] <= 2
 conflict_free_upper_1_BBU_13_A_0_1_21_arr_rightBBU_13_A_0_1_21_dep_leftBBU_13_A_200_2_21_arr_rightBBU_13_A_200_2_21_dep_left:
   p[BBU_13_A_0_1_21_arr_right,BBU_13_A_0_1_21_dep_left]
   - p[BBU_13_A_0_1_21_arr_right,BBU_13_A_200_2_21_arr_right]
   + p[BBU_13_A_0_1_21_dep_left,BBU_13_A_200_2_21_arr_right]
   + 2 h[BBU_13_A_0_1_21_arr_right,BBU_13_A_0_1_21_dep_left]
   + 2 h[BBU_13_A_200_2_21_arr_right,BBU_13_A_200_2_21_dep_left] <= 4
 conflict_free_lower_2_BBU_13_A_0_1_21_arr_rightBBU_13_A_0_1_21_dep_leftBBU_13_A_200_2_21_arr_rightBBU_13_A_200_2_21_dep_left:
   - p[BBU_13_A_200_2_21_arr_right,BBU_13_A_200_2_21_dep_left]
   + p[BBU_13_A_200_2_21_arr_right,BBU_13_A_0_1_21_arr_right]
   - p[BBU_13_A_200_2_21_dep_left,BBU_13_A_0_1_21_arr_right]
   + h[BBU_13_A_0_1_21_arr_right,BBU_13_A_0_1_21_dep_left]
   + h[BBU_13_A_200_2_21_arr_right,BBU_13_A_200_2_21_dep_left] <= 2
 conflict_free_upper_2_BBU_13_A_0_1_21_arr_rightBBU_13_A_0_1_21_dep_leftBBU_13_A_200_2_21_arr_rightBBU_13_A_200_2_21_dep_left:
   p[BBU_13_A_200_2_21_arr_right,BBU_13_A_200_2_21_dep_left]
   - p[BBU_13_A_200_2_21_arr_right,BBU_13_A_0_1_21_arr_right]
   + p[BBU_13_A_200_2_21_dep_left,BBU_13_A_0_1_21_arr_right]
   + 2 h[BBU_13_A_0_1_21_arr_right,BBU_13_A_0_1_21_dep_left]
   + 2 h[BBU_13_A_200_2_21_arr_right,BBU_13_A_200_2_21_dep_left] <= 4
 headway_lower_bound_BBU_112_B_200_2_21_arr_rightBBU_112_B_0_1_21_arr_right_BBU_112_B_200_2_21_arr_rightBBU_112_B_200_2_21_dep_rightBBU_112_B_0_1_21_arr_rightBBU_112_B_0_1_21_dep_right:
   - 200 p[BBU_112_B_200_2_21_arr_right,BBU_112_B_0_1_21_arr_right]
   - pi[BBU_112_B_0_1_21_arr_right] + pi[BBU_112_B_200_2_21_arr_right]
   + 25 h[BBU_112_B_0_1_21_arr_right,BBU_112_B_0_1_21_dep_right]
   + 25 h[BBU_112_B_200_2_21_arr_right,BBU_112_B_200_2_21_dep_right] <= 25
 headway_upper_bound_BBU_112_B_200_2_21_arr_rightBBU_112_B_0_1_21_arr_right_BBU_112_B_200_2_21_arr_rightBBU_112_B_200_2_21_dep_rightBBU_112_B_0_1_21_arr_rightBBU_112_B_0_1_21_dep_right:
   200 p[BBU_112_B_200_2_21_arr_right,BBU_112_B_0_1_21_arr_right]
   + pi[BBU_112_B_0_1_21_arr_right] - pi[BBU_112_B_200_2_21_arr_right]
   + 175 h[BBU_112_B_0_1_21_arr_right,BBU_112_B_0_1_21_dep_right]
   + 175 h[BBU_112_B_200_2_21_arr_right,BBU_112_B_200_2_21_dep_right]
   <= 525
 modulo_i_BBU_112_B_200_2_21_arr_rightBBU_112_B_0_1_21_arr_right_BBU_112_B_200_2_21_arr_right_BBU_112_B_200_2_21_dep_right_BBU_112_B_0_1_21_arr_right_BBU_112_B_0_1_21_dep_right:
   p[BBU_112_B_200_2_21_arr_right,BBU_112_B_0_1_21_arr_right] <= 1
 headway_lower_bound_BBU_112_B_0_1_21_arr_rightBBU_112_B_200_2_21_arr_right_BBU_112_B_200_2_21_arr_rightBBU_112_B_200_2_21_dep_rightBBU_112_B_0_1_21_arr_rightBBU_112_B_0_1_21_dep_right:
   - 200 p[BBU_112_B_0_1_21_arr_right,BBU_112_B_200_2_21_arr_right]
   + pi[BBU_112_B_0_1_21_arr_right] - pi[BBU_112_B_200_2_21_arr_right]
   + 25 h[BBU_112_B_0_1_21_arr_right,BBU_112_B_0_1_21_dep_right]
   + 25 h[BBU_112_B_200_2_21_arr_right,BBU_112_B_200_2_21_dep_right] <= 25
 headway_upper_bound_BBU_112_B_0_1_21_arr_rightBBU_112_B_200_2_21_arr_right_BBU_112_B_200_2_21_arr_rightBBU_112_B_200_2_21_dep_rightBBU_112_B_0_1_21_arr_rightBBU_112_B_0_1_21_dep_right:
   200 p[BBU_112_B_0_1_21_arr_right,BBU_112_B_200_2_21_arr_right]
   - pi[BBU_112_B_0_1_21_arr_right] + pi[BBU_112_B_200_2_21_arr_right]
   + 175 h[BBU_112_B_0_1_21_arr_right,BBU_112_B_0_1_21_dep_right]
   + 175 h[BBU_112_B_200_2_21_arr_right,BBU_112_B_200_2_21_dep_right]
   <= 525
 modulo_i_BBU_112_B_0_1_21_arr_rightBBU_112_B_200_2_21_arr_right_BBU_112_B_200_2_21_arr_right_BBU_112_B_200_2_21_dep_right_BBU_112_B_0_1_21_arr_right_BBU_112_B_0_1_21_dep_right:
   p[BBU_112_B_0_1_21_arr_right,BBU_112_B_200_2_21_arr_right] <= 1
 headway_lower_bound_BBU_112_B_200_2_21_dep_rightBBU_112_B_0_1_21_arr_right_BBU_112_B_200_2_21_arr_rightBBU_112_B_200_2_21_dep_rightBBU_112_B_0_1_21_arr_rightBBU_112_B_0_1_21_dep_right:
   - 200 p[BBU_112_B_200_2_21_dep_right,BBU_112_B_0_1_21_arr_right]
   - pi[BBU_112_B_0_1_21_arr_right] + pi[BBU_112_B_200_2_21_dep_right]
   + 17 h[BBU_112_B_0_1_21_arr_right,BBU_112_B_0_1_21_dep_right]
   + 17 h[BBU_112_B_200_2_21_arr_right,BBU_112_B_200_2_21_dep_right] <= 17
 headway_upper_bound_BBU_112_B_200_2_21_dep_rightBBU_112_B_0_1_21_arr_right_BBU_112_B_200_2_21_arr_rightBBU_112_B_200_2_21_dep_rightBBU_112_B_0_1_21_arr_rightBBU_112_B_0_1_21_dep_right:
   200 p[BBU_112_B_200_2_21_dep_right,BBU_112_B_0_1_21_arr_right]
   + pi[BBU_112_B_0_1_21_arr_right] - pi[BBU_112_B_200_2_21_dep_right]
   + 183 h[BBU_112_B_0_1_21_arr_right,BBU_112_B_0_1_21_dep_right]
   + 183 h[BBU_112_B_200_2_21_arr_right,BBU_112_B_200_2_21_dep_right]
   <= 549
 modulo_i_BBU_112_B_200_2_21_dep_rightBBU_112_B_0_1_21_arr_right_BBU_112_B_200_2_21_arr_right_BBU_112_B_200_2_21_dep_right_BBU_112_B_0_1_21_arr_right_BBU_112_B_0_1_21_dep_right:
   p[BBU_112_B_200_2_21_dep_right,BBU_112_B_0_1_21_arr_right] <= 1
 headway_lower_bound_BBU_112_B_0_1_21_dep_rightBBU_112_B_200_2_21_arr_right_BBU_112_B_200_2_21_arr_rightBBU_112_B_200_2_21_dep_rightBBU_112_B_0_1_21_arr_rightBBU_112_B_0_1_21_dep_right:
   - 200 p[BBU_112_B_0_1_21_dep_right,BBU_112_B_200_2_21_arr_right]
   + pi[BBU_112_B_0_1_21_dep_right] - pi[BBU_112_B_200_2_21_arr_right]
   + 17 h[BBU_112_B_0_1_21_arr_right,BBU_112_B_0_1_21_dep_right]
   + 17 h[BBU_112_B_200_2_21_arr_right,BBU_112_B_200_2_21_dep_right] <= 17
 headway_upper_bound_BBU_112_B_0_1_21_dep_rightBBU_112_B_200_2_21_arr_right_BBU_112_B_200_2_21_arr_rightBBU_112_B_200_2_21_dep_rightBBU_112_B_0_1_21_arr_rightBBU_112_B_0_1_21_dep_right:
   200 p[BBU_112_B_0_1_21_dep_right,BBU_112_B_200_2_21_arr_right]
   - pi[BBU_112_B_0_1_21_dep_right] + pi[BBU_112_B_200_2_21_arr_right]
   + 183 h[BBU_112_B_0_1_21_arr_right,BBU_112_B_0_1_21_dep_right]
   + 183 h[BBU_112_B_200_2_21_arr_right,BBU_112_B_200_2_21_dep_right]
   <= 549
 modulo_i_BBU_112_B_0_1_21_dep_rightBBU_112_B_200_2_21_arr_right_BBU_112_B_200_2_21_arr_right_BBU_112_B_200_2_21_dep_right_BBU_112_B_0_1_21_arr_right_BBU_112_B_0_1_21_dep_right:
   p[BBU_112_B_0_1_21_dep_right,BBU_112_B_200_2_21_arr_right] <= 1
 conflict_free_lower_1_BBU_112_B_200_2_21_arr_rightBBU_112_B_200_2_21_dep_rightBBU_112_B_0_1_21_arr_rightBBU_112_B_0_1_21_dep_right:
   - p[BBU_112_B_200_2_21_arr_right,BBU_112_B_200_2_21_dep_right]
   + p[BBU_112_B_200_2_21_arr_right,BBU_112_B_0_1_21_arr_right]
   - p[BBU_112_B_200_2_21_dep_right,BBU_112_B_0_1_21_arr_right]
   + h[BBU_112_B_0_1_21_arr_right,BBU_112_B_0_1_21_dep_right]
   + h[BBU_112_B_200_2_21_arr_right,BBU_112_B_200_2_21_dep_right] <= 2
 conflict_free_upper_1_BBU_112_B_200_2_21_arr_rightBBU_112_B_200_2_21_dep_rightBBU_112_B_0_1_21_arr_rightBBU_112_B_0_1_21_dep_right:
   p[BBU_112_B_200_2_21_arr_right,BBU_112_B_200_2_21_dep_right]
   - p[BBU_112_B_200_2_21_arr_right,BBU_112_B_0_1_21_arr_right]
   + p[BBU_112_B_200_2_21_dep_right,BBU_112_B_0_1_21_arr_right]
   + 2 h[BBU_112_B_0_1_21_arr_right,BBU_112_B_0_1_21_dep_right]
   + 2 h[BBU_112_B_200_2_21_arr_right,BBU_112_B_200_2_21_dep_right] <= 4
 conflict_free_lower_2_BBU_112_B_200_2_21_arr_rightBBU_112_B_200_2_21_dep_rightBBU_112_B_0_1_21_arr_rightBBU_112_B_0_1_21_dep_right:
   - p[BBU_112_B_0_1_21_arr_right,BBU_112_B_0_1_21_dep_right]
   + p[BBU_112_B_0_1_21_arr_right,BBU_112_B_200_2_21_arr_right]
   - p[BBU_112_B_0_1_21_dep_right,BBU_112_B_200_2_21_arr_right]
   + h[BBU_112_B_0_1_21_arr_right,BBU_112_B_0_1_21_dep_right]
   + h[BBU_112_B_200_2_21_arr_right,BBU_112_B_200_2_21_dep_right] <= 2
 conflict_free_upper_2_BBU_112_B_200_2_21_arr_rightBBU_112_B_200_2_21_dep_rightBBU_112_B_0_1_21_arr_rightBBU_112_B_0_1_21_dep_right:
   p[BBU_112_B_0_1_21_arr_right,BBU_112_B_0_1_21_dep_right]
   - p[BBU_112_B_0_1_21_arr_right,BBU_112_B_200_2_21_arr_right]
   + p[BBU_112_B_0_1_21_dep_right,BBU_112_B_200_2_21_arr_right]
   + 2 h[BBU_112_B_0_1_21_arr_right,BBU_112_B_0_1_21_dep_right]
   + 2 h[BBU_112_B_200_2_21_arr_right,BBU_112_B_200_2_21_dep_right] <= 4
 headway_lower_bound_BBU_111_B_200_2_21_arr_rightBBU_111_B_0_1_21_arr_right_BBU_111_B_200_2_21_arr_rightBBU_111_B_200_2_21_dep_rightBBU_111_B_0_1_21_arr_rightBBU_111_B_0_1_21_dep_right:
   - 200 p[BBU_111_B_200_2_21_arr_right,BBU_111_B_0_1_21_arr_right]
   - pi[BBU_111_B_0_1_21_arr_right] + pi[BBU_111_B_200_2_21_arr_right]
   + 25 h[BBU_111_B_0_1_21_arr_right,BBU_111_B_0_1_21_dep_right]
   + 25 h[BBU_111_B_200_2_21_arr_right,BBU_111_B_200_2_21_dep_right] <= 25
 headway_upper_bound_BBU_111_B_200_2_21_arr_rightBBU_111_B_0_1_21_arr_right_BBU_111_B_200_2_21_arr_rightBBU_111_B_200_2_21_dep_rightBBU_111_B_0_1_21_arr_rightBBU_111_B_0_1_21_dep_right:
   200 p[BBU_111_B_200_2_21_arr_right,BBU_111_B_0_1_21_arr_right]
   + pi[BBU_111_B_0_1_21_arr_right] - pi[BBU_111_B_200_2_21_arr_right]
   + 175 h[BBU_111_B_0_1_21_arr_right,BBU_111_B_0_1_21_dep_right]
   + 175 h[BBU_111_B_200_2_21_arr_right,BBU_111_B_200_2_21_dep_right]
   <= 525
 modulo_i_BBU_111_B_200_2_21_arr_rightBBU_111_B_0_1_21_arr_right_BBU_111_B_200_2_21_arr_right_BBU_111_B_200_2_21_dep_right_BBU_111_B_0_1_21_arr_right_BBU_111_B_0_1_21_dep_right:
   p[BBU_111_B_200_2_21_arr_right,BBU_111_B_0_1_21_arr_right] <= 1
 headway_lower_bound_BBU_111_B_0_1_21_arr_rightBBU_111_B_200_2_21_arr_right_BBU_111_B_200_2_21_arr_rightBBU_111_B_200_2_21_dep_rightBBU_111_B_0_1_21_arr_rightBBU_111_B_0_1_21_dep_right:
   - 200 p[BBU_111_B_0_1_21_arr_right,BBU_111_B_200_2_21_arr_right]
   + pi[BBU_111_B_0_1_21_arr_right] - pi[BBU_111_B_200_2_21_arr_right]
   + 25 h[BBU_111_B_0_1_21_arr_right,BBU_111_B_0_1_21_dep_right]
   + 25 h[BBU_111_B_200_2_21_arr_right,BBU_111_B_200_2_21_dep_right] <= 25
 headway_upper_bound_BBU_111_B_0_1_21_arr_rightBBU_111_B_200_2_21_arr_right_BBU_111_B_200_2_21_arr_rightBBU_111_B_200_2_21_dep_rightBBU_111_B_0_1_21_arr_rightBBU_111_B_0_1_21_dep_right:
   200 p[BBU_111_B_0_1_21_arr_right,BBU_111_B_200_2_21_arr_right]
   - pi[BBU_111_B_0_1_21_arr_right] + pi[BBU_111_B_200_2_21_arr_right]
   + 175 h[BBU_111_B_0_1_21_arr_right,BBU_111_B_0_1_21_dep_right]
   + 175 h[BBU_111_B_200_2_21_arr_right,BBU_111_B_200_2_21_dep_right]
   <= 525
 modulo_i_BBU_111_B_0_1_21_arr_rightBBU_111_B_200_2_21_arr_right_BBU_111_B_200_2_21_arr_right_BBU_111_B_200_2_21_dep_right_BBU_111_B_0_1_21_arr_right_BBU_111_B_0_1_21_dep_right:
   p[BBU_111_B_0_1_21_arr_right,BBU_111_B_200_2_21_arr_right] <= 1
 headway_lower_bound_BBU_111_B_200_2_21_dep_rightBBU_111_B_0_1_21_arr_right_BBU_111_B_200_2_21_arr_rightBBU_111_B_200_2_21_dep_rightBBU_111_B_0_1_21_arr_rightBBU_111_B_0_1_21_dep_right:
   - 200 p[BBU_111_B_200_2_21_dep_right,BBU_111_B_0_1_21_arr_right]
   - pi[BBU_111_B_0_1_21_arr_right] + pi[BBU_111_B_200_2_21_dep_right]
   + 17 h[BBU_111_B_0_1_21_arr_right,BBU_111_B_0_1_21_dep_right]
   + 17 h[BBU_111_B_200_2_21_arr_right,BBU_111_B_200_2_21_dep_right] <= 17
 headway_upper_bound_BBU_111_B_200_2_21_dep_rightBBU_111_B_0_1_21_arr_right_BBU_111_B_200_2_21_arr_rightBBU_111_B_200_2_21_dep_rightBBU_111_B_0_1_21_arr_rightBBU_111_B_0_1_21_dep_right:
   200 p[BBU_111_B_200_2_21_dep_right,BBU_111_B_0_1_21_arr_right]
   + pi[BBU_111_B_0_1_21_arr_right] - pi[BBU_111_B_200_2_21_dep_right]
   + 183 h[BBU_111_B_0_1_21_arr_right,BBU_111_B_0_1_21_dep_right]
   + 183 h[BBU_111_B_200_2_21_arr_right,BBU_111_B_200_2_21_dep_right]
   <= 549
 modulo_i_BBU_111_B_200_2_21_dep_rightBBU_111_B_0_1_21_arr_right_BBU_111_B_200_2_21_arr_right_BBU_111_B_200_2_21_dep_right_BBU_111_B_0_1_21_arr_right_BBU_111_B_0_1_21_dep_right:
   p[BBU_111_B_200_2_21_dep_right,BBU_111_B_0_1_21_arr_right] <= 1
 headway_lower_bound_BBU_111_B_0_1_21_dep_rightBBU_111_B_200_2_21_arr_right_BBU_111_B_200_2_21_arr_rightBBU_111_B_200_2_21_dep_rightBBU_111_B_0_1_21_arr_rightBBU_111_B_0_1_21_dep_right:
   - 200 p[BBU_111_B_0_1_21_dep_right,BBU_111_B_200_2_21_arr_right]
   + pi[BBU_111_B_0_1_21_dep_right] - pi[BBU_111_B_200_2_21_arr_right]
   + 17 h[BBU_111_B_0_1_21_arr_right,BBU_111_B_0_1_21_dep_right]
   + 17 h[BBU_111_B_200_2_21_arr_right,BBU_111_B_200_2_21_dep_right] <= 17
 headway_upper_bound_BBU_111_B_0_1_21_dep_rightBBU_111_B_200_2_21_arr_right_BBU_111_B_200_2_21_arr_rightBBU_111_B_200_2_21_dep_rightBBU_111_B_0_1_21_arr_rightBBU_111_B_0_1_21_dep_right:
   200 p[BBU_111_B_0_1_21_dep_right,BBU_111_B_200_2_21_arr_right]
   - pi[BBU_111_B_0_1_21_dep_right] + pi[BBU_111_B_200_2_21_arr_right]
   + 183 h[BBU_111_B_0_1_21_arr_right,BBU_111_B_0_1_21_dep_right]
   + 183 h[BBU_111_B_200_2_21_arr_right,BBU_111_B_200_2_21_dep_right]
   <= 549
 modulo_i_BBU_111_B_0_1_21_dep_rightBBU_111_B_200_2_21_arr_right_BBU_111_B_200_2_21_arr_right_BBU_111_B_200_2_21_dep_right_BBU_111_B_0_1_21_arr_right_BBU_111_B_0_1_21_dep_right:
   p[BBU_111_B_0_1_21_dep_right,BBU_111_B_200_2_21_arr_right] <= 1
 conflict_free_lower_1_BBU_111_B_200_2_21_arr_rightBBU_111_B_200_2_21_dep_rightBBU_111_B_0_1_21_arr_rightBBU_111_B_0_1_21_dep_right:
   - p[BBU_111_B_200_2_21_dep_right,BBU_111_B_0_1_21_arr_right]
   - p[BBU_111_B_200_2_21_arr_right,BBU_111_B_200_2_21_dep_right]
   + p[BBU_111_B_200_2_21_arr_right,BBU_111_B_0_1_21_arr_right]
   + h[BBU_111_B_0_1_21_arr_right,BBU_111_B_0_1_21_dep_right]
   + h[BBU_111_B_200_2_21_arr_right,BBU_111_B_200_2_21_dep_right] <= 2
 conflict_free_upper_1_BBU_111_B_200_2_21_arr_rightBBU_111_B_200_2_21_dep_rightBBU_111_B_0_1_21_arr_rightBBU_111_B_0_1_21_dep_right:
   p[BBU_111_B_200_2_21_dep_right,BBU_111_B_0_1_21_arr_right]
   + p[BBU_111_B_200_2_21_arr_right,BBU_111_B_200_2_21_dep_right]
   - p[BBU_111_B_200_2_21_arr_right,BBU_111_B_0_1_21_arr_right]
   + 2 h[BBU_111_B_0_1_21_arr_right,BBU_111_B_0_1_21_dep_right]
   + 2 h[BBU_111_B_200_2_21_arr_right,BBU_111_B_200_2_21_dep_right] <= 4
 conflict_free_lower_2_BBU_111_B_200_2_21_arr_rightBBU_111_B_200_2_21_dep_rightBBU_111_B_0_1_21_arr_rightBBU_111_B_0_1_21_dep_right:
   - p[BBU_111_B_0_1_21_dep_right,BBU_111_B_200_2_21_arr_right]
   - p[BBU_111_B_0_1_21_arr_right,BBU_111_B_0_1_21_dep_right]
   + p[BBU_111_B_0_1_21_arr_right,BBU_111_B_200_2_21_arr_right]
   + h[BBU_111_B_0_1_21_arr_right,BBU_111_B_0_1_21_dep_right]
   + h[BBU_111_B_200_2_21_arr_right,BBU_111_B_200_2_21_dep_right] <= 2
 conflict_free_upper_2_BBU_111_B_200_2_21_arr_rightBBU_111_B_200_2_21_dep_rightBBU_111_B_0_1_21_arr_rightBBU_111_B_0_1_21_dep_right:
   p[BBU_111_B_0_1_21_dep_right,BBU_111_B_200_2_21_arr_right]
   + p[BBU_111_B_0_1_21_arr_right,BBU_111_B_0_1_21_dep_right]
   - p[BBU_111_B_0_1_21_arr_right,BBU_111_B_200_2_21_arr_right]
   + 2 h[BBU_111_B_0_1_21_arr_right,BBU_111_B_0_1_21_dep_right]
   + 2 h[BBU_111_B_200_2_21_arr_right,BBU_111_B_200_2_21_dep_right] <= 4
 fix_henkel_henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12:
   pi[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12] = 0
 fix_henkel_henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12:
   pi[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12] = 0
 fix_henkel_henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12:
   pi[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12] = 0
 fix_henkel_henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12:
   pi[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12] = 0
 sheaf_0: b[0] = 1
 sheaf_1: b[1] + b[2] = 1
 sheaf_2: b[3] + b[4] = 1
 R127: - y_bar[BBU_111_B_0_1_21_dep_right,BBU_13_A_0_1_21_arr_right]
   - y_bar[BBU_13_A_0_1_21_arr_right,BBU_13_A_0_1_21_dep_left]
   - y_bar[BBU_13_A_0_1_21_dep_left,BBU_112_B_0_1_21_arr_right]
   - y_bar[BBU_112_B_0_1_21_arr_right,BBU_112_B_0_1_21_dep_right]
   - 2 y_bar[BBU_112_B_0_1_21_dep_right,henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12]
   - 2 y_bar[BBU_112_B_0_1_21_dep_right,henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12]
   - 2 y_bar[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12,BBU_111_B_0_1_21_arr_right]
   - 2 y_bar[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12,BBU_111_B_0_1_21_arr_right]
   - y_bar[BBU_111_B_0_1_21_arr_right,BBU_111_B_0_1_21_dep_right]
   - y_bar[BBU_111_B_200_2_21_dep_right,BBU_13_A_200_2_21_arr_right]
   - y_bar[BBU_13_A_200_2_21_arr_right,BBU_13_A_200_2_21_dep_left]
   - y_bar[BBU_13_A_200_2_21_dep_left,BBU_112_B_200_2_21_arr_right]
   - y_bar[BBU_112_B_200_2_21_arr_right,BBU_112_B_200_2_21_dep_right]
   - 2 y_bar[BBU_112_B_200_2_21_dep_right,henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12]
   - 2 y_bar[BBU_112_B_200_2_21_dep_right,henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12]
   - 2 y_bar[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12,BBU_111_B_200_2_21_arr_right]
   - 2 y_bar[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12,BBU_111_B_200_2_21_arr_right]
   - y_bar[BBU_111_B_200_2_21_arr_right,BBU_111_B_200_2_21_dep_right]
   - 15 h[BBU_111_B_0_1_21_dep_right,BBU_13_A_0_1_21_arr_right]
   - 20 h[BBU_13_A_0_1_21_arr_right,BBU_13_A_0_1_21_dep_left]
   - 15 h[BBU_13_A_0_1_21_dep_left,BBU_112_B_0_1_21_arr_right]
   - 5 h[BBU_112_B_0_1_21_arr_right,BBU_112_B_0_1_21_dep_right]
   - 122 h[BBU_112_B_0_1_21_dep_right,henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12]
   - 322 h[BBU_112_B_0_1_21_dep_right,henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12]
   - 60 h[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12,BBU_111_B_0_1_21_arr_right]
   - 260 h[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12,BBU_111_B_0_1_21_arr_right]
   - 5 h[BBU_111_B_0_1_21_arr_right,BBU_111_B_0_1_21_dep_right]
   - 15 h[BBU_111_B_200_2_21_dep_right,BBU_13_A_200_2_21_arr_right]
   - 20 h[BBU_13_A_200_2_21_arr_right,BBU_13_A_200_2_21_dep_left]
   - 15 h[BBU_13_A_200_2_21_dep_left,BBU_112_B_200_2_21_arr_right]
   - 5 h[BBU_112_B_200_2_21_arr_right,BBU_112_B_200_2_21_dep_right]
   - 122 h[BBU_112_B_200_2_21_dep_right,henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12]
   - 322 h[BBU_112_B_200_2_21_dep_right,henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12]
   - 60 h[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12,BBU_111_B_200_2_21_arr_right]
   - 260 h[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12,BBU_111_B_200_2_21_arr_right]
   - 5 h[BBU_111_B_200_2_21_arr_right,BBU_111_B_200_2_21_dep_right] + obj
   = 0
 R128: h[BBU_111_B_0_1_21_dep_right,BBU_13_A_0_1_21_arr_right] - b[1]
   - b[2] + L[BBU_111_B_0_1_21_dep_right,BBU_13_A_0_1_21_arr_right] = 0
 h_inequality_BBU_111_B_0_1_21_dep_right_BBU_13_A_0_1_21_arr_right:
   h[BBU_111_B_0_1_21_dep_right,BBU_13_A_0_1_21_arr_right] - b[1] - b[2]
   <= 0
 R130: h[BBU_13_A_0_1_21_arr_right,BBU_13_A_0_1_21_dep_left] - b[1] - b[2]
   + L[BBU_13_A_0_1_21_arr_right,BBU_13_A_0_1_21_dep_left] = 0
 h_inequality_BBU_13_A_0_1_21_arr_right_BBU_13_A_0_1_21_dep_left:
   h[BBU_13_A_0_1_21_arr_right,BBU_13_A_0_1_21_dep_left] - b[1] - b[2]
   <= 0
 R132: h[BBU_13_A_0_1_21_dep_left,BBU_112_B_0_1_21_arr_right] - b[1] - b[2]
   + L[BBU_13_A_0_1_21_dep_left,BBU_112_B_0_1_21_arr_right] = 0
 h_inequality_BBU_13_A_0_1_21_dep_left_BBU_112_B_0_1_21_arr_right:
   h[BBU_13_A_0_1_21_dep_left,BBU_112_B_0_1_21_arr_right] - b[1] - b[2]
   <= 0
 R134: h[BBU_112_B_0_1_21_arr_right,BBU_112_B_0_1_21_dep_right] - b[1]
   - b[2] + L[BBU_112_B_0_1_21_arr_right,BBU_112_B_0_1_21_dep_right] = 0
 h_inequality_BBU_112_B_0_1_21_arr_right_BBU_112_B_0_1_21_dep_right:
   h[BBU_112_B_0_1_21_arr_right,BBU_112_B_0_1_21_dep_right] - b[1] - b[2]
   <= 0
 R136:
   h[BBU_112_B_0_1_21_dep_right,henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12]
   - b[2]
   + L[BBU_112_B_0_1_21_dep_right,henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12]
   = 0
 h_inequality_BBU_112_B_0_1_21_dep_right_henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12:
   h[BBU_112_B_0_1_21_dep_right,henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12]
   - b[2] <= 0
 R138:
   h[BBU_112_B_0_1_21_dep_right,henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12]
   - b[1]
   + L[BBU_112_B_0_1_21_dep_right,henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12]
   = 0
 h_inequality_BBU_112_B_0_1_21_dep_right_henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12:
   h[BBU_112_B_0_1_21_dep_right,henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12]
   - b[1] <= 0
 R140:
   h[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12,BBU_111_B_0_1_21_arr_right]
   - b[2]
   + L[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12,BBU_111_B_0_1_21_arr_right]
   = 0
 h_inequality_henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12_BBU_111_B_0_1_21_arr_right:
   h[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12,BBU_111_B_0_1_21_arr_right]
   - b[2] <= 0
 R142:
   h[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12,BBU_111_B_0_1_21_arr_right]
   - b[1]
   + L[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12,BBU_111_B_0_1_21_arr_right]
   = 0
 h_inequality_henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12_BBU_111_B_0_1_21_arr_right:
   h[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12,BBU_111_B_0_1_21_arr_right]
   - b[1] <= 0
 R144: h[BBU_111_B_0_1_21_arr_right,BBU_111_B_0_1_21_dep_right] - b[1]
   - b[2] + L[BBU_111_B_0_1_21_arr_right,BBU_111_B_0_1_21_dep_right] = 0
 h_inequality_BBU_111_B_0_1_21_arr_right_BBU_111_B_0_1_21_dep_right:
   h[BBU_111_B_0_1_21_arr_right,BBU_111_B_0_1_21_dep_right] - b[1] - b[2]
   <= 0
 R146: h[BBU_111_B_200_2_21_dep_right,BBU_13_A_200_2_21_arr_right] - b[3]
   - b[4] + L[BBU_111_B_200_2_21_dep_right,BBU_13_A_200_2_21_arr_right]
   = 0
 h_inequality_BBU_111_B_200_2_21_dep_right_BBU_13_A_200_2_21_arr_right:
   h[BBU_111_B_200_2_21_dep_right,BBU_13_A_200_2_21_arr_right] - b[3]
   - b[4] <= 0
 R148: h[BBU_13_A_200_2_21_arr_right,BBU_13_A_200_2_21_dep_left] - b[3]
   - b[4] + L[BBU_13_A_200_2_21_arr_right,BBU_13_A_200_2_21_dep_left] = 0
 h_inequality_BBU_13_A_200_2_21_arr_right_BBU_13_A_200_2_21_dep_left:
   h[BBU_13_A_200_2_21_arr_right,BBU_13_A_200_2_21_dep_left] - b[3] - b[4]
   <= 0
 R150: h[BBU_13_A_200_2_21_dep_left,BBU_112_B_200_2_21_arr_right] - b[3]
   - b[4] + L[BBU_13_A_200_2_21_dep_left,BBU_112_B_200_2_21_arr_right] = 0
 h_inequality_BBU_13_A_200_2_21_dep_left_BBU_112_B_200_2_21_arr_right:
   h[BBU_13_A_200_2_21_dep_left,BBU_112_B_200_2_21_arr_right] - b[3] - b[4]
   <= 0
 R152: h[BBU_112_B_200_2_21_arr_right,BBU_112_B_200_2_21_dep_right] - b[3]
   - b[4] + L[BBU_112_B_200_2_21_arr_right,BBU_112_B_200_2_21_dep_right]
   = 0
 h_inequality_BBU_112_B_200_2_21_arr_right_BBU_112_B_200_2_21_dep_right:
   h[BBU_112_B_200_2_21_arr_right,BBU_112_B_200_2_21_dep_right] - b[3]
   - b[4] <= 0
 R154:
   h[BBU_112_B_200_2_21_dep_right,henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12]
   - b[4]
   + L[BBU_112_B_200_2_21_dep_right,henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12]
   = 0
 h_inequality_BBU_112_B_200_2_21_dep_right_henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12:
   h[BBU_112_B_200_2_21_dep_right,henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12]
   - b[4] <= 0
 R156:
   h[BBU_112_B_200_2_21_dep_right,henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12]
   - b[3]
   + L[BBU_112_B_200_2_21_dep_right,henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12]
   = 0
 h_inequality_BBU_112_B_200_2_21_dep_right_henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12:
   h[BBU_112_B_200_2_21_dep_right,henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12]
   - b[3] <= 0
 R158:
   h[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12,BBU_111_B_200_2_21_arr_right]
   - b[4]
   + L[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12,BBU_111_B_200_2_21_arr_right]
   = 0
 h_inequality_henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12_BBU_111_B_200_2_21_arr_right:
   h[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12,BBU_111_B_200_2_21_arr_right]
   - b[4] <= 0
 R160:
   h[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12,BBU_111_B_200_2_21_arr_right]
   - b[3]
   + L[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12,BBU_111_B_200_2_21_arr_right]
   = 0
 h_inequality_henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12_BBU_111_B_200_2_21_arr_right:
   h[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12,BBU_111_B_200_2_21_arr_right]
   - b[3] <= 0
 R162: h[BBU_111_B_200_2_21_arr_right,BBU_111_B_200_2_21_dep_right] - b[3]
   - b[4] + L[BBU_111_B_200_2_21_arr_right,BBU_111_B_200_2_21_dep_right]
   = 0
 h_inequality_BBU_111_B_200_2_21_arr_right_BBU_111_B_200_2_21_dep_right:
   h[BBU_111_B_200_2_21_arr_right,BBU_111_B_200_2_21_dep_right] - b[3]
   - b[4] <= 0
 arc_activation_BBU_111_B_0_1_21_dep_rightBBU_13_A_0_1_21_arr_right:
   - h[BBU_111_B_0_1_21_dep_right,BBU_13_A_0_1_21_arr_right] + b[1] + b[2]
   <= 0
 arc_activation_BBU_13_A_0_1_21_arr_rightBBU_13_A_0_1_21_dep_left:
   - h[BBU_13_A_0_1_21_arr_right,BBU_13_A_0_1_21_dep_left] + b[1] + b[2]
   <= 0
 arc_activation_BBU_13_A_0_1_21_dep_leftBBU_112_B_0_1_21_arr_right:
   - h[BBU_13_A_0_1_21_dep_left,BBU_112_B_0_1_21_arr_right] + b[1] + b[2]
   <= 0
 arc_activation_BBU_112_B_0_1_21_arr_rightBBU_112_B_0_1_21_dep_right:
   - h[BBU_112_B_0_1_21_arr_right,BBU_112_B_0_1_21_dep_right] + b[1] + b[2]
   <= 0
 arc_activation_BBU_112_B_0_1_21_dep_righthenkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12:
   - h[BBU_112_B_0_1_21_dep_right,henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12]
   + b[1] <= 0
 arc_activation_henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12BBU_111_B_0_1_21_arr_right:
   - h[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12,BBU_111_B_0_1_21_arr_right]
   + b[2] <= 0
 arc_activation_henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12BBU_111_B_0_1_21_arr_right:
   - h[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12,BBU_111_B_0_1_21_arr_right]
   + b[1] <= 0
 arc_activation_BBU_111_B_0_1_21_arr_rightBBU_111_B_0_1_21_dep_right:
   - h[BBU_111_B_0_1_21_arr_right,BBU_111_B_0_1_21_dep_right] + b[1] + b[2]
   <= 0
 arc_activation_BBU_111_B_200_2_21_dep_rightBBU_13_A_200_2_21_arr_right:
   - h[BBU_111_B_200_2_21_dep_right,BBU_13_A_200_2_21_arr_right] + b[3]
   + b[4] <= 0
 arc_activation_BBU_13_A_200_2_21_arr_rightBBU_13_A_200_2_21_dep_left:
   - h[BBU_13_A_200_2_21_arr_right,BBU_13_A_200_2_21_dep_left] + b[3]
   + b[4] <= 0
 arc_activation_BBU_13_A_200_2_21_dep_leftBBU_112_B_200_2_21_arr_right:
   - h[BBU_13_A_200_2_21_dep_left,BBU_112_B_200_2_21_arr_right] + b[3]
   + b[4] <= 0
 arc_activation_BBU_112_B_200_2_21_arr_rightBBU_112_B_200_2_21_dep_right:
   - h[BBU_112_B_200_2_21_arr_right,BBU_112_B_200_2_21_dep_right] + b[3]
   + b[4] <= 0
 arc_activation_BBU_112_B_200_2_21_dep_righthenkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12:
   - h[BBU_112_B_200_2_21_dep_right,henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12]
   + b[4] <= 0
 arc_activation_BBU_112_B_200_2_21_dep_righthenkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12:
   - h[BBU_112_B_200_2_21_dep_right,henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12]
   + b[3] <= 0
 arc_activation_henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12BBU_111_B_200_2_21_arr_right:
   - h[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12,BBU_111_B_200_2_21_arr_right]
   + b[3] <= 0
 arc_activation_BBU_111_B_200_2_21_arr_rightBBU_111_B_200_2_21_dep_right:
   - h[BBU_111_B_200_2_21_arr_right,BBU_111_B_200_2_21_dep_right] + b[3]
   + b[4] <= 0
Bounds
 p[BBU_111_B_0_1_21_dep_right,BBU_13_A_0_1_21_arr_right] <= 1
 p[BBU_111_B_0_1_21_dep_right,BBU_111_B_200_2_21_arr_right] <= 1
 p[BBU_13_A_0_1_21_arr_right,BBU_13_A_0_1_21_dep_left] <= 1
 p[BBU_13_A_0_1_21_arr_right,BBU_13_A_200_2_21_arr_right] <= 1
 p[BBU_13_A_0_1_21_dep_left,BBU_112_B_0_1_21_arr_right] <= 1
 p[BBU_13_A_0_1_21_dep_left,BBU_13_A_200_2_21_arr_right] <= 1
 p[BBU_112_B_0_1_21_arr_right,BBU_112_B_0_1_21_dep_right] <= 1
 p[BBU_112_B_0_1_21_arr_right,BBU_112_B_200_2_21_arr_right] <= 1
 p[BBU_112_B_0_1_21_dep_right,henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12] <= 1
 p[BBU_112_B_0_1_21_dep_right,henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12] <= 1
 p[BBU_112_B_0_1_21_dep_right,BBU_112_B_200_2_21_arr_right] <= 1
 p[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12,BBU_111_B_0_1_21_arr_right] <= 1
 p[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12,BBU_111_B_0_1_21_arr_right] <= 1
 p[BBU_111_B_0_1_21_arr_right,BBU_111_B_0_1_21_dep_right] <= 1
 p[BBU_111_B_0_1_21_arr_right,BBU_111_B_200_2_21_arr_right] <= 1
 p[BBU_111_B_200_2_21_dep_right,BBU_13_A_200_2_21_arr_right] <= 1
 p[BBU_111_B_200_2_21_dep_right,BBU_111_B_0_1_21_arr_right] <= 1
 p[BBU_13_A_200_2_21_arr_right,BBU_13_A_200_2_21_dep_left] <= 1
 p[BBU_13_A_200_2_21_arr_right,BBU_13_A_0_1_21_arr_right] <= 1
 p[BBU_13_A_200_2_21_dep_left,BBU_112_B_200_2_21_arr_right] <= 1
 p[BBU_13_A_200_2_21_dep_left,BBU_13_A_0_1_21_arr_right] <= 1
 p[BBU_112_B_200_2_21_arr_right,BBU_112_B_200_2_21_dep_right] <= 1
 p[BBU_112_B_200_2_21_arr_right,BBU_112_B_0_1_21_arr_right] <= 1
 p[BBU_112_B_200_2_21_dep_right,henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12] <= 1
 p[BBU_112_B_200_2_21_dep_right,henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12] <= 1
 p[BBU_112_B_200_2_21_dep_right,BBU_112_B_0_1_21_arr_right] <= 1
 p[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12,BBU_111_B_200_2_21_arr_right] <= 1
 p[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12,BBU_111_B_200_2_21_arr_right] <= 1
 p[BBU_111_B_200_2_21_arr_right,BBU_111_B_200_2_21_dep_right] <= 1
 p[BBU_111_B_200_2_21_arr_right,BBU_111_B_0_1_21_arr_right] <= 1
 pi[BBU_111_B_0_1_21_dep_right] <= 199
 pi[BBU_13_A_0_1_21_arr_right] <= 199
 pi[BBU_13_A_0_1_21_dep_left] <= 199
 pi[BBU_112_B_0_1_21_arr_right] <= 199
 pi[BBU_112_B_0_1_21_dep_right] <= 199
 pi[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12] <= 199
 pi[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12] <= 199
 pi[BBU_111_B_0_1_21_arr_right] <= 199
 pi[BBU_111_B_200_2_21_dep_right] <= 199
 pi[BBU_13_A_200_2_21_arr_right] <= 199
 pi[BBU_13_A_200_2_21_dep_left] <= 199
 pi[BBU_112_B_200_2_21_arr_right] <= 199
 pi[BBU_112_B_200_2_21_dep_right] <= 199
 pi[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12] <= 199
 pi[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12] <= 199
 pi[BBU_111_B_200_2_21_arr_right] <= 199
 L[BBU_111_B_0_1_21_dep_right,BBU_13_A_0_1_21_arr_right] free
 L[BBU_13_A_0_1_21_arr_right,BBU_13_A_0_1_21_dep_left] free
 L[BBU_13_A_0_1_21_dep_left,BBU_112_B_0_1_21_arr_right] free
 L[BBU_112_B_0_1_21_arr_right,BBU_112_B_0_1_21_dep_right] free
 L[BBU_112_B_0_1_21_dep_right,henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12] free
 L[BBU_112_B_0_1_21_dep_right,henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12] free
 L[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12,BBU_111_B_0_1_21_arr_right] free
 L[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12,BBU_111_B_0_1_21_arr_right] free
 L[BBU_111_B_0_1_21_arr_right,BBU_111_B_0_1_21_dep_right] free
 L[BBU_111_B_200_2_21_dep_right,BBU_13_A_200_2_21_arr_right] free
 L[BBU_13_A_200_2_21_arr_right,BBU_13_A_200_2_21_dep_left] free
 L[BBU_13_A_200_2_21_dep_left,BBU_112_B_200_2_21_arr_right] free
 L[BBU_112_B_200_2_21_arr_right,BBU_112_B_200_2_21_dep_right] free
 L[BBU_112_B_200_2_21_dep_right,henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12] free
 L[BBU_112_B_200_2_21_dep_right,henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12] free
 L[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12,BBU_111_B_200_2_21_arr_right] free
 L[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12,BBU_111_B_200_2_21_arr_right] free
 L[BBU_111_B_200_2_21_arr_right,BBU_111_B_200_2_21_dep_right] free
Binaries
 h[BBU_111_B_0_1_21_dep_right,BBU_13_A_0_1_21_arr_right]
 h[BBU_13_A_0_1_21_arr_right,BBU_13_A_0_1_21_dep_left]
 h[BBU_13_A_0_1_21_dep_left,BBU_112_B_0_1_21_arr_right]
 h[BBU_112_B_0_1_21_arr_right,BBU_112_B_0_1_21_dep_right]
 h[BBU_112_B_0_1_21_dep_right,henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12]
 h[BBU_112_B_0_1_21_dep_right,henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12]
 h[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12,BBU_111_B_0_1_21_arr_right]
 h[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12,BBU_111_B_0_1_21_arr_right]
 h[BBU_111_B_0_1_21_arr_right,BBU_111_B_0_1_21_dep_right]
 h[BBU_111_B_200_2_21_dep_right,BBU_13_A_200_2_21_arr_right]
 h[BBU_13_A_200_2_21_arr_right,BBU_13_A_200_2_21_dep_left]
 h[BBU_13_A_200_2_21_dep_left,BBU_112_B_200_2_21_arr_right]
 h[BBU_112_B_200_2_21_arr_right,BBU_112_B_200_2_21_dep_right]
 h[BBU_112_B_200_2_21_dep_right,henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12]
 h[BBU_112_B_200_2_21_dep_right,henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12]
 h[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12,BBU_111_B_200_2_21_arr_right]
 h[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12,BBU_111_B_200_2_21_arr_right]
 h[BBU_111_B_200_2_21_arr_right,BBU_111_B_200_2_21_dep_right] b[0] b[1]
 b[2] b[3] b[4]
Generals
 p[BBU_111_B_0_1_21_dep_right,BBU_13_A_0_1_21_arr_right]
 p[BBU_111_B_0_1_21_dep_right,BBU_111_B_200_2_21_arr_right]
 p[BBU_13_A_0_1_21_arr_right,BBU_13_A_0_1_21_dep_left]
 p[BBU_13_A_0_1_21_arr_right,BBU_13_A_200_2_21_arr_right]
 p[BBU_13_A_0_1_21_dep_left,BBU_112_B_0_1_21_arr_right]
 p[BBU_13_A_0_1_21_dep_left,BBU_13_A_200_2_21_arr_right]
 p[BBU_112_B_0_1_21_arr_right,BBU_112_B_0_1_21_dep_right]
 p[BBU_112_B_0_1_21_arr_right,BBU_112_B_200_2_21_arr_right]
 p[BBU_112_B_0_1_21_dep_right,henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12]
 p[BBU_112_B_0_1_21_dep_right,henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12]
 p[BBU_112_B_0_1_21_dep_right,BBU_112_B_200_2_21_arr_right]
 p[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12,BBU_111_B_0_1_21_arr_right]
 p[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12,BBU_111_B_0_1_21_arr_right]
 p[BBU_111_B_0_1_21_arr_right,BBU_111_B_0_1_21_dep_right]
 p[BBU_111_B_0_1_21_arr_right,BBU_111_B_200_2_21_arr_right]
 p[BBU_111_B_200_2_21_dep_right,BBU_13_A_200_2_21_arr_right]
 p[BBU_111_B_200_2_21_dep_right,BBU_111_B_0_1_21_arr_right]
 p[BBU_13_A_200_2_21_arr_right,BBU_13_A_200_2_21_dep_left]
 p[BBU_13_A_200_2_21_arr_right,BBU_13_A_0_1_21_arr_right]
 p[BBU_13_A_200_2_21_dep_left,BBU_112_B_200_2_21_arr_right]
 p[BBU_13_A_200_2_21_dep_left,BBU_13_A_0_1_21_arr_right]
 p[BBU_112_B_200_2_21_arr_right,BBU_112_B_200_2_21_dep_right]
 p[BBU_112_B_200_2_21_arr_right,BBU_112_B_0_1_21_arr_right]
 p[BBU_112_B_200_2_21_dep_right,henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12]
 p[BBU_112_B_200_2_21_dep_right,henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12]
 p[BBU_112_B_200_2_21_dep_right,BBU_112_B_0_1_21_arr_right]
 p[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12,BBU_111_B_200_2_21_arr_right]
 p[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12,BBU_111_B_200_2_21_arr_right]
 p[BBU_111_B_200_2_21_arr_right,BBU_111_B_200_2_21_dep_right]
 p[BBU_111_B_200_2_21_arr_right,BBU_111_B_0_1_21_arr_right]
End
