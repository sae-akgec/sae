import { Injectable } from "@angular/core";
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { DOMAIN } from "../shared/assets";
/**
 * @description
 * @class
 */
@Injectable()
export class UserService {

  domain = DOMAIN
  authToken: any;
  email: any;
  username: any;
  constructor(private http: HttpClient) {
    const token = 
    this.authToken = localStorage.getItem('id_token');
    this.email = localStorage.getItem('email');
    this.username = localStorage.getItem('username')
  }

  registerUser(user) {
    const headers = new HttpHeaders({ 'Content-Type': 'application/json; charset=utf-8' });
    return this.http.post(this.domain + '/api/v1/auth/register/', user, { headers: headers });
  }
  loginUser(user) {
    const headers = new HttpHeaders({ 'Content-Type': 'application/json; charset=utf-8' });
    return this.http.post(this.domain + '/api/v1/auth/login/', user, { headers: headers });
  }

  getClassroom() {
    const headers = new HttpHeaders(
      {
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': 'JWT ' + this.authToken
      });
    return this.http.get(this.domain + '/api/v1/user/classroom/', { headers: headers });
  }
  getCourse(id:number) {
    const headers = new HttpHeaders(
      {
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': 'JWT ' + this.authToken
      });
    return this.http.get(this.domain + '/api/v1/user/classroom/' + id + '/', { headers: headers });
  }
  getCurrentWorkshops(){
    const headers = new HttpHeaders(
      {
        'Content-Type': 'application/json; charset=utf-8'
      });
    return this.http.get(this.domain + '/api/v1/workshops/latest/', {headers:headers})
  }
  postEnrollment(data) {
    const headers = new HttpHeaders(
      {
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': 'JWT ' + this.authToken
      });
    return this.http.post(this.domain + '/api/v1/user/enroll/',data, { headers: headers });
  }
}
