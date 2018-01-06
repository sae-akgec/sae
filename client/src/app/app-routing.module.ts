import { NgModule } from "@angular/core"
import { RouterModule, Routes } from "@angular/router";
import { MainComponent } from "./home/main/main.component";
import { ContactComponent } from "./home/contact/contact.component";

const routes: Routes = [
     {path:'', component:MainComponent},
     {path:'contact', component:ContactComponent}
]

@NgModule({
    imports:[RouterModule.forRoot(routes)],
    exports:[RouterModule]
})

export class AppRoutingModule {

}