from django.db import models

COUNTY_CHOICE = (
    (1	, 'Alba	'),
    (2	, 'Arad	'),
    (3	, 'Argeș'),
    (4	, 'Bacău'),
    (5	, 'Bihor'),
    (6	, 'Bistrița-Năsăud'),
    (7	, 'Botoșani'),
    (8	, 'Brașov'),
    (9	, 'Brăila'),
    (10	, 'București'),
    (11	, 'Buzău'),
    (12	, 'Caraș-Severin'),
    (13	, 'Călărași'),
    (14	, 'Cluj'),
    (15	, 'Constanța'),
    (16	, 'Covasna'),
    (17	, 'Dâmbovița'),
    (18	, 'Dolj'),
    (19	, 'Galați'),
    (20	, 'Giurgiu'),
    (21	, 'Gorj'),
    (22	, 'Harghita'),
    (23	, 'Hunedoara'),
    (24	, 'Ialomița'),
    (25	, 'Iași'),
    (26	, 'Ilfov'),
    (27	, 'Maramureș	'),
    (28	, 'Mehedinți'),
    (29	, 'Mureș'),
    (30	, 'Neamț'),
    (31	, 'Olt'),
    (32	, 'Prahova'),
    (33	, 'Satu Mare'),
    (34	, 'Sălaj	'),
    (35	, 'Sibiu	'),
    (36	, 'Suceava'),
    (37	, 'Teleorman'),
    (38	, 'Timiș'),
    (39	, 'Tulcea'),
    (40	, 'Vaslui'),
    (41	, 'Vâlcea')
)


class UserTypeChoice(models.IntegerChoices):
    # The Patient, doctor and secretary will belong to one or more specialties
    PATIENT = 1, 'Patient'
    DOCTOR = 2, 'Doctor'
    SECRETARY = 3, 'Secretary'
    # The admin will be able to manage information from any specialty
    ADMIN = 4, 'Admin'
