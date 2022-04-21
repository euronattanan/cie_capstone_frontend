import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { FormArray, FormBuilder, FormGroup, Validators } from '@angular/forms';
import { NgxSpinnerService } from 'ngx-spinner';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent implements OnInit {
  public qrdata: string = null;
  vaccineForm: FormGroup;
  numberOfVaccine: number[] = [2, 3];
  vaccineList: string[] = [
    'Pfizer',
    'Sinovac',
    'Astrazeneca',
    'Moderna',
    'Sinopharm',
  ];

  doses: Array<string> = [];
  imageurl: string =
    'https://th.qr-code-generator.com/wp-content/themes/qr/new_structure/markets/basic_market/generator/dist/generator/assets/images/websiteQRCode_noFrame.png';
  isShowImage: boolean = false;
  countdown: any;
  time: number;
  constructor(
    private fb: FormBuilder,
    private spinner: NgxSpinnerService,
    private http: HttpClient
  ) {}

  ngOnInit(): void {
    this.buildForm();
  }

  buildForm() {
    this.vaccineForm = this.fb.group({
      firstName: [null, Validators.required],
      lastName: [null, Validators.required],
      contact: [null, Validators.required],
      numberOfVaccines: [null, Validators.required],
      doses: new FormArray([]),
    });
  }

  // convenience getters for easy access to form fields
  get f() {
    return this.vaccineForm.controls;
  }
  get t() {
    return this.f.doses as FormArray;
  }
  get vaccineFormGroups() {
    return this.t.controls as FormGroup[];
  }

  onChangeVaccines(e) {
    const numberOfVaccines = e.value || 0;
    if (this.t.length < numberOfVaccines) {
      for (let i = this.t.length; i < numberOfVaccines; i++) {
        this.t.push(
          this.fb.group({
            vaccine: [null, Validators.required],
          })
        );
      }
    } else {
      for (let i = this.t.length; i >= numberOfVaccines; i--) {
        this.t.removeAt(i);
      }
    }
  }

  onSaveVaccine() {
    this.doses = [];
    if (this.vaccineForm.valid) {
      if (this.vaccineForm.value.doses.length > 0) {
        for (let i = 0; i < this.vaccineForm.value.doses.length; i++) {
          this.doses.push(this.vaccineForm.value.doses[i]['vaccine']);
        }
      }

      this.vaccineForm.value.doses = this.doses;

      // Send to Euro
      this.http.post('url', this.vaccineForm.value).subscribe({
        next: (response: any) => {
          console.log(response);
          // ยัดมาในนี้
        },
        error: (err: any) => {
          console.log(err);
        },
      });

      // start Move
      this.qrdata = JSON.stringify(this.vaccineForm.value);

      this.spinner.show();
      this.isShowImage = true;

      setTimeout(() => {
        scrollTo(0, document.body.scrollHeight);
        this.spinner.hide();
      }, 800);

      clearInterval(this.countdown);

      this.time = 180;
      this.countdown = setInterval(() => {
        this.time--;
        if (this.time < 0) {
          clearInterval(this.countdown);
        }
      }, 1000);

      setTimeout(() => {
        this.isShowImage = false;
      }, 180000);

      this.buildForm();
      // End move
    } else {
      alert('Please fill all fields');
    }
  }

  // onCancel() {
  //   this.vaccineForm.reset();
  //   this.onChangeVaccines(0);
  // }
}
