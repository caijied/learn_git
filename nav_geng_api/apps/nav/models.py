from django.db import models


class Car(models.Model):
    """
        车辆
    """

    name = models.CharField(verbose_name='车辆名称', max_length=32, null=False, blank=False)
    unit_type = models.CharField(verbose_name='车辆型号', max_length=32, null=False, blank=False)
    empty_quality = models.FloatField(verbose_name='空车质量', default=0)
    full_payload_weight = models.FloatField(verbose_name='满载总重', default=0)
    max_speed = models.FloatField(verbose_name='最高车速（KM/H）', default=0)
    min_turning_radius = models.FloatField(verbose_name='最小转弯半径（M）', default=0)
    overall_length = models.FloatField(verbose_name='全长（mm）', default=0)
    overall_width = models.FloatField(verbose_name='总宽（mm）', default=0)
    noload_height = models.FloatField(verbose_name='空载高度（mm）', default=0)
    add_time = models.DateTimeField(verbose_name='加入时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    def __str__(self):
        return f'{self.name}-{self.unit_type}'

    class Meta:
        verbose_name = '车辆'
        verbose_name_plural = '车辆'
        ordering = ['-add_time']


class VPM(models.Model):
    """
        车队
    """

    name = models.CharField(verbose_name='车队名称', max_length=32, null=False, blank=False)
    sn = models.CharField(verbose_name='车队编号', max_length=32, null=False, blank=False)
    leader_id = models.IntegerField(verbose_name='车队领头车ID', null=True, blank=True)
    member = models.ManyToManyField(verbose_name='成员', to='Car', blank=True)
    add_time = models.DateTimeField(verbose_name='加入时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    def __str__(self):
        return f'{self.name}-{self.sn}'

    def set_leader(self, leader_id):
        try:
            leader = self.member.get(pk=leader_id)
            if leader is not None:
                self.leader_id = int(leader_id)
        except Car.DoesNotExist as e:
            pass

    class Meta:
        verbose_name = '车队'
        verbose_name_plural = '车队'
        ordering = ['-add_time']
        unique_together = ['name', 'sn']


class NavigationTask(models.Model):
    """
        导航任务
    """

    cur_pos = models.CharField(verbose_name='当前位置', max_length=32)
    target_pos = models.CharField(verbose_name='目标位置', max_length=32)
    vpm = models.ForeignKey(verbose_name='导航任务绑定车队', to='VPM', on_delete=models.DO_NOTHING)
    car = models.ForeignKey(verbose_name='导航任务绑定车辆', to='Car', on_delete=models.DO_NOTHING)
    status = models.IntegerField(verbose_name='导航状态', choices=((0, '导航中'), (1, '导航完成')), default=0)
    add_time = models.DateTimeField(verbose_name='加入时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    class Meta:
        verbose_name = '导航任务'
        verbose_name_plural = '导航任务'
        ordering = ['-add_time']
        unique_together = ['car', 'vpm']
