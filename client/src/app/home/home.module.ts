import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule,ReactiveFormsModule } from "@angular/forms";
import { RouterModule } from "@angular/router";

import { MainComponent } from './main/main.component';
import { ContactComponent } from "./contact/contact.component";
import { EventComponent } from "./event/event.component";
import { TeamComponent } from "./team/team.component";
import { WorkshopComponent } from "./workshop/workshop.component";
import { MainService } from "./services/main.service";


@NgModule({
  declarations: [
    MainComponent, ContactComponent, EventComponent, TeamComponent,WorkshopComponent
  ],
  imports: [
    CommonModule, HttpClientModule, FormsModule, ReactiveFormsModule, RouterModule
  ],
  providers: [MainService]
})
export class HomeModule { }
