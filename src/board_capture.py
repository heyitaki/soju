import cv2
import numpy as np

temp_path = "data/sample_images/hex_masks.jpg"


# Input: Screenshot defined as 3/4 channel Numpy array
def board_read(screenshot, mask_path=temp_path):
    board = cv2.imread(screenshot)
    mask = cv2.imread(mask_path)
    mask_inv = cv2.bitwise_not(mask)
    rows, cols, channels = board.shape
    board = board[0:rows, 0:cols]

    # Scale mask to same size as image
    mask_rows, mask_cols, mask_channels = mask_inv.shape
    mask_inv = mask_inv[0:mask_rows, 0:mask_cols, :1]
    delta_w = cols - mask_cols
    delta_h = rows - mask_rows

    top, bottom = delta_h // 2, delta_h - (delta_h // 2)
    left, right = delta_w // 2, delta_w - (delta_w // 2)
    scaled_mask = cv2.copyMakeBorder(mask_inv, top, bottom, left, right, cv2.BORDER_REPLICATE)

    cut_board = cv2.bitwise_or(board, board, mask=scaled_mask)
    ''' 
    # TODO
    Iterate through cut_board for each hex
    Compare each image to a sample champion model
    '''
    return cut_board


if __name__ == 'main':
    board_out = board_read("data/sample_images/board_sample.png")
    cv2.imshow("image", board_out)
    cv2.waitKey(0)




