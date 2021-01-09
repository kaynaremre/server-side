#!/usr/bin/env python3

import boto3
import sys

def detect_labels_local_file(photo):

    client=boto3.client('rekognition')

    with open(photo, 'rb') as image:
        response = client.detect_protective_equipment(Image={'Bytes': image.read()},
            SummarizationAttributes={'MinConfidence':80, 'RequiredEquipmentTypes':['FACE_COVER']})

    # print('Detected PPE for people in image ' + photo) 
    # print('\nDetected people\n---------------')   
    # for person in response['Persons']:
        
        # print('Person ID: ' + str(person['Id']))
        # print ('Body Parts\n----------')
        # body_parts = person['BodyParts']
        # if len(body_parts) == 0:
                # print ('No body parts found')
        # else:
            # for body_part in body_parts:
                # print('\t'+ body_part['Name'] + '\n\t\tConfidence: ' + str(body_part['Confidence']))
                # print('\n\t\tDetected PPE\n\t\t------------')
                # ppe_items = body_part['EquipmentDetections']
                # if len(ppe_items) ==0:
                    # print ('\t\tNo PPE detected on ' + body_part['Name'])
                # else:    
                    # for ppe_item in ppe_items:
                        # print('\t\t' + ppe_item['Type'] + '\n\t\t\tConfidence: ' + str(ppe_item['Confidence'])) 
                        # print('\t\tCovers body part: ' + str(ppe_item['CoversBodyPart']['Value']) + '\n\t\t\tConfidence: ' + str(ppe_item['CoversBodyPart']['Confidence']))
                        # print('\t\tBounding Box:')
                        # print ('\t\t\tTop: ' + str(ppe_item['BoundingBox']['Top']))
                        # print ('\t\t\tLeft: ' + str(ppe_item['BoundingBox']['Left']))
                        # print ('\t\t\tWidth: ' +  str(ppe_item['BoundingBox']['Width']))
                        # print ('\t\t\tHeight: ' +  str(ppe_item['BoundingBox']['Height']))
                        # print ('\t\t\tConfidence: ' + str(ppe_item['Confidence']))
            # print()
        # print()

    #print('Person ID Summary\n----------------')
    #display_summary('With required equipment',response['Summary']['PersonsWithRequiredEquipment'] )
    display_summary('Without required equipment',response['Summary']['PersonsWithoutRequiredEquipment'] )
    #display_summary('Indeterminate',response['Summary']['PersonsIndeterminate'] )
    #print(response)
    return len(response['Persons'])

#Display summary information for supplied summary.
def display_summary(summary_type, summary):
    #print (summary_type + '\n\tIDs: ',end='')
    if (len(summary)==0):
        print('No person identificated without face mask')
    else:
        print('There are people without mask !')
        for i in summary:
            print("IDs", i)


def main():

    photo = sys.argv[1]

    person_count=detect_labels_local_file(photo)
    #print("Persons detected: " + str(person_count))

if __name__ == "__main__":
    main()
    