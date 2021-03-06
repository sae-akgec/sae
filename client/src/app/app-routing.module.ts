import { NgModule } from "@angular/core"
import { RouterModule, Routes } from "@angular/router";

// Main Module Component
import { MainComponent } from "./home/main/main.component";
import { ContactComponent } from "./home/contact/contact.component";
import { TeamComponent } from "./home/team/team.component";
import { WorkshopComponent } from "./home/workshop/workshop.component";
import { EventComponent } from "./home/event/event.component";

// Auth Module Component
import { SigninComponent } from "./auth/signin/signin.component";
import { SignupComponent } from "./auth/signup/signup.component";
import { ResetComponent } from "./auth/reset/reset.component";
import { AuthService } from "./auth/auth.service";
import { AuthComponent } from "./auth/auth.component";

// User Module Component
import { ClassroomComponent } from "./user/classroom/classroom.component";
import { CourseComponent } from "./user/course/course.component";
import { RegisterComponent } from "./user/register/register.component";
import { UserComponent } from "./user/user.component";
import { PaymentComponent } from "./user/payment/payment.component";

// Shared Component
import { Error404Component } from "./shared/error404/error404.component";

// Auth Gaurd
import { AuthGaurd } from "./auth/auth-gaurd.service";

const routes: Routes = [
    { path: '', component: MainComponent },
    { path: 'contact', component: ContactComponent },
    { path: 'team', component: TeamComponent },
    { path: 'workshop/:name', component: WorkshopComponent },
    { path: 'event/:id', component: EventComponent },
    {
        path: 'auth', component: AuthComponent, children: [
            { path: 'signin', component: SigninComponent },
            { path: 'signup', component: SignupComponent },
            { path: 'reset', component: ResetComponent },
        ]
    },
    {
        path: 'user', component: UserComponent, canActivate: [AuthGaurd], children: [
            { path: 'classroom', component: ClassroomComponent },
            { path: 'course/:id', component: CourseComponent },
            { path: 'register', component: RegisterComponent },
            { path: 'payment', component: PaymentComponent }
        ]
    },
    { path: '**', component: Error404Component }
]

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})

export class AppRoutingModule {

}