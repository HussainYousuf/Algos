import base64
import time
import boto3
import cv2

STREAM_NAME = "testing"
kvs = boto3.client("kinesisvideo")
rekognition = boto3.client('rekognition')
# Grab the endpoint from GetDataEndpoint
endpoint = kvs.get_data_endpoint(
    APIName="GET_HLS_STREAMING_SESSION_URL",
    StreamName=STREAM_NAME
)['DataEndpoint']

print(endpoint)

# # Grab the HLS Stream URL from the endpoint
kvam = boto3.client("kinesis-video-archived-media", endpoint_url=endpoint)
url = kvam.get_hls_streaming_session_url(
    StreamName=STREAM_NAME,
    PlaybackMode="LIVE"
)['HLSStreamingSessionURL']


vcap = cv2.VideoCapture(url)
count = 0
while(True):
    # Capture frame-by-frame
    # vcap.set(cv2.CAP_PROP_POS_MSEC,(count*20))
    # count += 1
    ret, frame = vcap.read()

    if frame is not None:
        # Display the resulting frame
        # print(frame)
        
        height, width, _ = frame.shape
        # img_encoded = cv2.imencode('.jpg', frame)[1]
        # res = rekognition.detect_protective_equipment(Image={'Bytes': img_encoded.tobytes()})
        # try:
        #     # print(res)
        #     x = list(
        #             filter(
        #                 lambda a: a["Name"] == "HEAD",
        #                 res["Persons"][0]["BodyParts"]
        #             )
        #         )[0]
        #     x = x["EquipmentDetections"][0]
        #     # print(res)
        #     Width = x["BoundingBox"]["Width"] * width
        #     Height = x["BoundingBox"]["Height"] * height
        #     Left = x["BoundingBox"]["Left"] * width
        #     Top = x["BoundingBox"]["Top"] * height
        #     print(Width, Height, Left, Top)
        #     cv2.rectangle(frame,(int(Left), int(Top)),(int(Left + Width), int(Top + Height)), (255,0,0), 2)
            
        # except Exception as e:
        #     print(e)

        cv2.imshow('frame', frame)
        # break
        # Press q to close the video windows before it ends if you want
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    else:
        print("Frame is None")
        break

    # time.sleep(1)

# When everything done, release the capture
vcap.release()
cv2.destroyAllWindows()
print("Video stop")