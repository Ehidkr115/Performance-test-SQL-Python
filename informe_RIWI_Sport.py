from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import black, lightgrey
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT

def generate_executive_report(file_name="RIWI_Sport_Executive_Report.pdf"):
    """
    Generates a PDF document with an executive summary, KPIs, insight, and recommendation.
    """
    # 1. Document Configuration
    doc = SimpleDocTemplate(
        file_name,
        pagesize=letter,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=72
    )
    
    Story = []
    
    # 2. Get and Customize Styles
    styles = getSampleStyleSheet()
    
    # Base Styles
    style_title = styles['Title']
    style_h1 = styles['Heading1']
    style_h2 = styles['Heading2']
    style_body = styles['Normal']
    
    # Body Style Customization
    style_body.fontSize = 10
    style_body.leading = 14
    style_body.spaceAfter = 6
    style_body.alignment = TA_JUSTIFY

    # Specific style for Recommendation lines (for list indentation)
    style_list = ParagraphStyle(
        'ListStyle',
        parent=style_body,
        leftIndent=0.3 * inch,
        firstLineIndent=-0.3 * inch,
        bulletIndent=0,
        bulletFontName='Helvetica-Bold',
        bulletFontSize=10,
        alignment=TA_LEFT
    )

    # ----------------------------------------------------
    # DOCUMENT CONTENT
    # ----------------------------------------------------

    # Main Title
    Story.append(Paragraph("<b>Sales Analysis and Recommendations Report</b>", style_title))
    Story.append(Spacer(1, 0.5 * inch))

    # ===============================================
    # EXECUTIVE SUMMARY
    # ===============================================
    
    Story.append(Paragraph("<b># 📊 Executive Summary</b>", style_h1))
    Story.append(Spacer(1, 0.1 * inch))
    
    summary_text = """
    The analysis of <b>RIWI Sport's</b> sales data reveals clear behavioral patterns among customers and product categories.
    The <b>Training</b> category leads in total revenue, while <b>Running</b> shows significant price variability, indicating segmentation potential between budget and premium consumers.
    Customer spending also varies by city: higher-income cities not only generate more sales but also show a higher <b>Average Order Value (AOV)</b>, suggesting that product type and purchasing power are geographically correlated.
    <br/><br/>
    Overall, RIWI Sport demonstrates a diverse customer base and a broad product offering, with opportunities to enhance revenue through segmentation, dynamic pricing, and regional marketing strategies.
    """
    Story.append(Paragraph(summary_text, style_body))
    Story.append(Spacer(1, 0.3 * inch))

    # ===============================================
    # KPIs (Table)
    # ===============================================
    
    Story.append(Paragraph("<b># 📈 Key Performance Indicators (KPIs)</b>", style_h1))
    Story.append(Spacer(1, 0.1 * inch))

    # KPI Table Data
    kpi_data = [
        [Paragraph("<b>KPI</b>", styles['BodyText']), Paragraph("<b>Description</b>", styles['BodyText']), Paragraph("<b>Result (Example / Expected)</b>", styles['BodyText'])],
        ['<b>Average Order Value (AOV)</b>', 'Mean customer spend per order', '$125.40'],
        ['<b>Median Spend per Customer</b>', 'Typical spending behavior', '$118.00'],
        ['<b>Mode of Spend per Customer</b>', 'Most frequent spending range', '$100–$110'],
        ['<b>Price Variability (Running)</b>', 'Std. deviation of prices in Running products', 'High (σ ≈ 75.3)'],
        ['<b>Top 5 Categories by Revenue</b>', 'Ranked by total sales', 'Training, Running, Outdoor, Yoga, Accessories'],
        ['<b>Top 5 Products by Quantity Sold</b>', 'Units sold', 'T-Shirt Basic, Training Shoes, Running Shorts, Yoga Mat, Water Bottle'],
        ['<b>Top Cities by Revenue</b>', 'Regional contribution', 'Bogotá, Medellín, Cali, Barranquilla, Cartagena'],
    ]

    # Creating the Table
    table_kpis = Table(kpi_data, colWidths=[2*inch, 2.5*inch, 2*inch])
    
    # Table Style
    style_table = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#F0F0F0')), # Light gray background for header
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('PADDING', (0, 0), (-1, -1), 6),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ])
    
    table_kpis.setStyle(style_table)
    Story.append(table_kpis)
    Story.append(Spacer(1, 0.3 * inch))

    # ===============================================
    # INSIGHT
    # ===============================================
    
    Story.append(Paragraph("<b>### Insight</b>", style_h2))
    Story.append(Spacer(1, 0.1 * inch))
    
    insight_text = """
    After analyzing total sales and price dispersion across categories, it was observed that the <b>Training</b> category concentrates the highest total revenue, while <b>Running</b> shows the greatest price variability (high standard deviation).
    This suggests that Running products range from affordable options to high-end items, attracting different customer segments.
    Additionally, cities with higher total revenue also exhibit a higher average ticket, reinforcing the idea that customer spending is related to the predominant product types in each local market.
    """
    Story.append(Paragraph(insight_text, style_body))
    Story.append(Spacer(1, 0.3 * inch))

    # ===============================================
    # RECOMMENDATION
    # ===============================================
    
    Story.append(Paragraph("<b>### Recommendation</b>", style_h2))
    Story.append(Spacer(1, 0.1 * inch))
    
    # Segmentation
    Story.append(Paragraph("Segment the <b>Running</b> category into two product lines:", style_body))
    
    # Basic Line
    Story.append(Paragraph(
        "&bull; <b>Basic Line:</b> focused on entry-level products, offering volume discounts or combo deals.",
        style_list
    ))
    
    # Premium Line
    Story.append(Paragraph(
        "&bull; <b>Premium Line:</b> positioned as aspirational, with training bundles and exclusive benefits.",
        style_list
    ))
    
    Story.append(Spacer(1, 0.15 * inch))
    
    # Regional Strategy
    recommendation_cities = """
    Furthermore, cities with <b>lower average tickets</b> should receive price-focused campaigns (discounts and combos), while those with <b>higher spending</b> should be targeted with value-added strategies (premium products, loyalty programs, or experiential offers).
    """
    Story.append(Paragraph(recommendation_cities, style_body))
    
    # 3. Build the PDF
    doc.build(Story)
    
    print(f"PDF '{file_name}' generated successfully.")

# Execute the function to create the PDF
generate_executive_report()