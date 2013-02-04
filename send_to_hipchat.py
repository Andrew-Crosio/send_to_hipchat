# coding=utf-8
"""Send to hipchat"""
import argparse
import urllib
import urllib2


parser = argparse.ArgumentParser(description='Send to hipchat')
parser.add_argument('-r', '--room', dest='room_id', type=int, required=True,
                    help='Room id to sent to')
parser.add_argument('-f', '--from', dest='user', type=str, required=True,
                    help='Name of from identity')
parser.add_argument('-m', '--message', dest='msg', type=str, required=True,
                    help='Message to send')
parser.add_argument('-F', '--format', dest='message_format', 
                    choices=['html', 'text'], required=False, default='html',
                    help='Format to send')
parser.add_argument('-c', '--colour', dest='colour',
                    choices=['yellow', 'red', 'green', 'purple', 'gray', 'random'],
                    required=False, default='yellow', help='Background colour')
parser.add_argument('-n', '--notify', dest='notify',choices=['1','0'],
                    required=False, default='1', help='Whether or not to notify')


def run():
    """send the message to hipchat"""
    arg_namespace = parser.parse_args()
    hipchat_data = {
        'room_id': str(arg_namespace.room_id),
        'from': arg_namespace.user,
        'message': arg_namespace.msg,
        'message_format': arg_namespace.message_format,
        'color': arg_namespace.colour,
        'notify': arg_namespace.notify
    }

    urlenc_data = urllib.urlencode(hipchat_data)
    hipchat_url = ('https://api.hipchat.com/v1/rooms/message/?auth_token=%s'
                   % AUTH_KEY)
    request = urllib2.Request(hipchat_url, data=urlenc_data)
    response = urllib2.urlopen(request)
    if response.msg == 'OK':
        print 'Successfully sent message'
    else:
        print 'Encountered error sending message'


if __name__ == '__main__':
    run()
