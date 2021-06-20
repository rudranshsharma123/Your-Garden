using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.XR.ARFoundation;

public class SpawnManager : MonoBehaviour
{

    [SerializeField] 
    ARRaycastManager m_RaycastManager; 
    List<ARRaycastHit> m_Hits = new List<ARRaycastHit>(); 
    [SerializeField] 
    public GameObject[] prefabs; 
    Camera arCam; 
    GameObject spawnedObject;
    GameObject spawnablePrefab;
    public void one(){
        spawnablePrefab = prefabs[0];
    }
  public void two(){
        spawnablePrefab = prefabs[1];
    }public void three(){
        spawnablePrefab = prefabs[2];
    }public void four(){
        spawnablePrefab = prefabs[3];
    }
    // }  
    // public void five(){
    //     spawnablePrefab = prefabs[4];
    // }
    // public void six(){
    //     spawnablePrefab = prefabs[5];
    // }
    // public void seven(){
    //     spawnablePrefab = prefabs[6];
    // }
    // public void eight(){
    //     spawnablePrefab = prefabs[7];
    // }
    // Start is called before the first frame update
    void Start()
    {
        spawnedObject = null; 
        arCam = GameObject.Find("AR Camera").GetComponent<Camera>();
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.touchCount == 0) return; 
        RaycastHit hit;
        Ray ray = arCam.ScreenPointToRay(Input.GetTouch(0).position);
        if (m_RaycastManager.Raycast(Input.GetTouch(0).position, m_Hits)) 
        { if(Input.GetTouch(0).phase == TouchPhase.Began && spawnedObject == null)
         { if (Physics.Raycast(ray, out hit))
          { if (hit.collider.gameObject.tag == "Spawnable") 
          { spawnedObject = hit.collider.gameObject; } 
          else { SpawnPrefab(m_Hits[0].pose.position);
           } } }
            else if(Input.GetTouch(0).phase == TouchPhase.Moved && spawnedObject != null) 
            { spawnedObject.transform.position = m_Hits[0].pose.position; } 
            if(Input.GetTouch(0).phase == TouchPhase.Ended) 
            { spawnedObject = null; } }
        
    }
private void SpawnPrefab(Vector3 spawnPosition) 
{ spawnedObject = Instantiate(spawnablePrefab, spawnPosition, Quaternion.identity); 
}

}
