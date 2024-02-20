# -*- coding: utf-8 -*-
from odoo import fields, models, api


class HrEmployeeInherit(models.Model):
    _inherit = 'hr.employee'
    _description = "Human Resource"

    father_name = fields.Char(string='ولد')
    grand_father_name = fields.Char(string='ولدیت')

    position = fields.Char(string='بست')
    job_step = fields.Char(string='قدم')
    recruitment_date = fields.Date(string='تاریخ تقرر در بست فعلی')
    # job_status = fields.Selection([('fire', 'منفک'), ('change', 'تبدیل'), ('recruiter', 'جدیدالتقرر')], string="حالت")

    start_date = fields.Date(string='تاریخ شروع')
    end_date = fields.Date(string='تاریخ ختم')
    education_location = fields.Char(string='محل تحصیل')
    university = fields.Char(string='پوهنتون')

    skill = fields.Char(string='نوع مهارت')
    major = fields.Char(string='تخصص')
    remarks = fields.Char(string='ملاحظات')

    course = fields.Char(string='کورس')
    training_type = fields.Char(string='نوعیت آموزش')
    training_location = fields.Char(string='محل آموزش')
    training_start_date = fields.Date(string='تاریخ شروع')
    training_end_date = fields.Date(string='تاریخ ختم')

    rewards_type = fields.Char(string='انواع مکافات / مجازات')
    reason_for_sentence = fields.Char(string='دلیل صدور حکم')
    date_of_sentence = fields.Char(string='تاریخ صدور حکم')
    order_no = fields.Char(string='نمبر حکم')

    organization = fields.Char(string='وزارت / اداره')
    job_position = fields.Char(string='عنوان وظیفه')
    grade = fields.Selection([('1st', 'اول'), ('2nd', 'دوم'), ('3rd', 'سوم'), ('4th', 'چهارم'), ('5th', 'پنجم'),
                              ('6th', 'ششم'), ('7th', 'هفتم'), ('8th', 'هشتم')], string="درجه / بست")
    step = fields.Selection([('1st', 'قدم اول'), ('2nd', 'قدم دوم'), ('3rd', 'قدم سوم'), ('4th', 'قدم چهارم'),
                             ('5th', 'قدم پنجم')], string="قدم")

    job_location = fields.Char(string='محل وظیفه')
    department = fields.Char(string='ریاست')
    status = fields.Char(string='حالت')
    # job_start_date = fields.Date(string='Start Date')
    # job_end_date = fields.Date(string='End Date')
    # service_duration = fields.Char(string='Service Duration')

    job_start_date = fields.Date(string='تاریخ شروع')
    job_end_date = fields.Date(string='تاریخ ختم')
    duration_days = fields.Integer('مدت خدمت (Days)', compute='_compute_duration_days', store=True)

    @api.depends('job_start_date', 'job_end_date')
    def _compute_duration_days(self):
        for record in self:
            if record.job_start_date and record.job_end_date:
                delta = record.job_end_date - record.job_start_date
                record.duration_days = delta.days
                # record.duration_years = delta.days
                # record.duration_months = delta.months
            else:
                record.duration_days = 0
                # record.duration_months = 0

    language = fields.Selection([('Dari', 'دری'), ('Pashto', 'پشتو'), ('English', 'انگلیسی'), ('Urdu', 'اردو'),
                             ('Arabic', 'عربی')], string="مهارت های زبان")
    reading = fields.Char(string='مهارت خواندن')
    writing = fields.Char(string='مهارت نوشتن')
    listening = fields.Char(string='مهارت فهمیدن')
    speaking = fields.Char(string='مهارت صحبت کردن')

    publication_type = fields.Selection([('Book', 'کتاب'), ('Magazine', 'مجله')], string="نوع انتشارات")
    subject = fields.Char(string='مضمون')
    publication_date = fields.Date(string='تاریخ چاپ')
    no_of_pages = fields.Char(string='تعداد صفحات')
    isbn = fields.Char(string='ISBN')





