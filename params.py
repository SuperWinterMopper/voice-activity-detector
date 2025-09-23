sample_rate = 16000

# 512 important here for speech processing, ~23ms for our data from Libriparty
windowed_signal_length = 512
num_mel_bands = 40

# means 1 / overlap ratio of overlap for each time frame. 
overlap = 2