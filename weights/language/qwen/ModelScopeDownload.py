from modelscope.hub.snapshot_download import snapshot_download

# 下载Qwen-14B-Chat
# model_dir = snapshot_download('qwen/Qwen-14B-Chat', cache_dir='/Users/motang/git/mrobot/weights/language', revision='v1.0.5')
# 下载Qwen-14B-Chat-Int4
model_dir = snapshot_download('qwen/Qwen-14B-Chat-Int4', cache_dir='/Users/motang/git/mrobot/weights/language', revision='v1.0.6')
