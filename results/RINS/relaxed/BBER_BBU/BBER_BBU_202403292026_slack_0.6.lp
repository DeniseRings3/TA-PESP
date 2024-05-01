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
   + 15 h[BBU_111_B_0_1_21_dep_right,BBU_13_A_0_1_21_arr_right]
   + 20 h[BBU_13_A_0_1_21_arr_right,BBU_13_A_0_1_21_dep_left]
   + 15 h[BBU_13_A_0_1_21_dep_left,BBU_112_B_0_1_21_arr_right]
   + 5 h[BBU_112_B_0_1_21_arr_right,BBU_112_B_0_1_21_dep_right]
   + 122 h[BBU_112_B_0_1_21_dep_right,henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12]
   + 322 h[BBU_112_B_0_1_21_dep_right,henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12]
   + 60 h[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12,BBU_111_B_0_1_21_arr_right]
   + 260 h[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12,BBU_111_B_0_1_21_arr_right]
   + 5 h[BBU_111_B_0_1_21_arr_right,BBU_111_B_0_1_21_dep_right]
   + 15 h[BBU_111_B_200_2_21_dep_right,BBU_13_A_200_2_21_arr_right]
   + 20 h[BBU_13_A_200_2_21_arr_right,BBU_13_A_200_2_21_dep_left]
   + 15 h[BBU_13_A_200_2_21_dep_left,BBU_112_B_200_2_21_arr_right]
   + 5 h[BBU_112_B_200_2_21_arr_right,BBU_112_B_200_2_21_dep_right]
   + 122 h[BBU_112_B_200_2_21_dep_right,henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12]
   + 322 h[BBU_112_B_200_2_21_dep_right,henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12]
   + 60 h[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12,BBU_111_B_200_2_21_arr_right]
   + 260 h[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12,BBU_111_B_200_2_21_arr_right]
   + 5 h[BBU_111_B_200_2_21_arr_right,BBU_111_B_200_2_21_dep_right]
Subject To
 objective_cutoff:
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
   + 15 h[BBU_111_B_0_1_21_dep_right,BBU_13_A_0_1_21_arr_right]
   + 20 h[BBU_13_A_0_1_21_arr_right,BBU_13_A_0_1_21_dep_left]
   + 15 h[BBU_13_A_0_1_21_dep_left,BBU_112_B_0_1_21_arr_right]
   + 5 h[BBU_112_B_0_1_21_arr_right,BBU_112_B_0_1_21_dep_right]
   + 122 h[BBU_112_B_0_1_21_dep_right,henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12]
   + 322 h[BBU_112_B_0_1_21_dep_right,henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12]
   + 60 h[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12,BBU_111_B_0_1_21_arr_right]
   + 260 h[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_0_1_12,BBU_111_B_0_1_21_arr_right]
   + 5 h[BBU_111_B_0_1_21_arr_right,BBU_111_B_0_1_21_dep_right]
   + 15 h[BBU_111_B_200_2_21_dep_right,BBU_13_A_200_2_21_arr_right]
   + 20 h[BBU_13_A_200_2_21_arr_right,BBU_13_A_200_2_21_dep_left]
   + 15 h[BBU_13_A_200_2_21_dep_left,BBU_112_B_200_2_21_arr_right]
   + 5 h[BBU_112_B_200_2_21_arr_right,BBU_112_B_200_2_21_dep_right]
   + 122 h[BBU_112_B_200_2_21_dep_right,henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12]
   + 322 h[BBU_112_B_200_2_21_dep_right,henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12]
   + 60 h[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12,BBU_111_B_200_2_21_arr_right]
   + 260 h[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12,BBU_111_B_200_2_21_arr_right]
   + 5 h[BBU_111_B_200_2_21_arr_right,BBU_111_B_200_2_21_dep_right]
   <= 972.18
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
 sheaf_0: b[0] = 1
 sheaf_1: b[1] + b[2] = 1
 sheaf_2: b[3] + b[4] = 1
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
 arc_activation_BBU_112_B_0_1_21_dep_righthenkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12:
   - h[BBU_112_B_0_1_21_dep_right,henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_0_1_12]
   + b[2] <= 0
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
 arc_activation_henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12BBU_111_B_200_2_21_arr_right:
   - h[henkel_0_S2_W_BBER_BLRD_0_S2_W_BLRD_BBER_0_200_2_12,BBU_111_B_200_2_21_arr_right]
   + b[4] <= 0
 arc_activation_henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12BBU_111_B_200_2_21_arr_right:
   - h[henkel_0_S2_WI_BBU_BLRD_0_S2_WI_BLRD_BBU_0_200_2_12,BBU_111_B_200_2_21_arr_right]
   + b[3] <= 0
 arc_activation_BBU_111_B_200_2_21_arr_rightBBU_111_B_200_2_21_dep_right:
   - h[BBU_111_B_200_2_21_arr_right,BBU_111_B_200_2_21_dep_right] + b[3]
   + b[4] <= 0
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
