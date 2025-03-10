import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-management-system",
    description="Meta package for oca-management-system Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-document_page_environment_manual>=16.0dev,<16.1dev',
        'odoo-addon-document_page_environmental_aspect>=16.0dev,<16.1dev',
        'odoo-addon-document_page_procedure>=16.0dev,<16.1dev',
        'odoo-addon-document_page_quality_manual>=16.0dev,<16.1dev',
        'odoo-addon-document_page_work_instruction>=16.0dev,<16.1dev',
        'odoo-addon-mgmtsystem>=16.0dev,<16.1dev',
        'odoo-addon-mgmtsystem_action>=16.0dev,<16.1dev',
        'odoo-addon-mgmtsystem_action_efficacy>=16.0dev,<16.1dev',
        'odoo-addon-mgmtsystem_action_template>=16.0dev,<16.1dev',
        'odoo-addon-mgmtsystem_audit>=16.0dev,<16.1dev',
        'odoo-addon-mgmtsystem_hazard>=16.0dev,<16.1dev',
        'odoo-addon-mgmtsystem_manual>=16.0dev,<16.1dev',
        'odoo-addon-mgmtsystem_nonconformity>=16.0dev,<16.1dev',
        'odoo-addon-mgmtsystem_nonconformity_hr>=16.0dev,<16.1dev',
        'odoo-addon-mgmtsystem_nonconformity_mrp>=16.0dev,<16.1dev',
        'odoo-addon-mgmtsystem_nonconformity_product>=16.0dev,<16.1dev',
        'odoo-addon-mgmtsystem_partner>=16.0dev,<16.1dev',
        'odoo-addon-mgmtsystem_review>=16.0dev,<16.1dev',
        'odoo-addon-mgmtsystem_survey>=16.0dev,<16.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 16.0',
    ]
)
